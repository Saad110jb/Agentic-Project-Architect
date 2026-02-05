import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crewai import Crew, Process, Task
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from database.mongo_db import MongoDB, save_roadmap
from agents.analyst import get_analyst_agent
from agents.researcher import get_researcher_agent
from agents.architect import get_architect_agent

load_dotenv()

# Ensure Groq Key is available
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

app = FastAPI(title="Agentic Project Architect API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RoadmapRequest(BaseModel):
    user_id: str
    github_username: str

@app.on_event("startup")
async def startup_db_client():
    await MongoDB.connect_to_storage()

@app.on_event("shutdown")
async def shutdown_db_client():
    await MongoDB.close_storage()

@app.post("/generate-roadmap")
async def generate_roadmap(request: RoadmapRequest):
    print(f"🚀 Request received for: {request.github_username}")
    try:
        # Initialize Agents (now using Groq)
        analyst = get_analyst_agent()
        researcher = get_researcher_agent()
        architect = get_architect_agent()

        analysis_task = Task(
            description=f"Analyze the GitHub profile of {request.github_username}. Identify top 3 skills and experience level.",
            expected_output="Structured summary of technical profile.",
            agent=analyst
        )

        research_task = Task(
    description=(
        f"1. Take the technical analysis for {request.github_username}.\n"
        "2. Use ONLY the 'trend_researcher' tool to find one relevant tech trend.\n"
        "3. DO NOT attempt to use any web search or 'brave_search'.\n"
        "4. If no trends are found in the tool, suggest a project based on 'Agentic AI Workflows' as a default."
    ),
    expected_output="A specific project concept and the trending technology to be used.",
    agent=researcher,
    context=[analysis_task]
    
)

        roadmap_task = Task(
    description=(
        "Using the concept: {research_output}, create a high-level 4-week project roadmap. "
        "Each week MUST have 3 specific technical milestones. "
        "The output MUST be in high-quality Markdown format. "
        "START the output with a bold Project Title. "
        "DO NOT include any conversational filler like 'Based on the analysis...' "
        "JUST output the Markdown roadmap."
    ),
    expected_output="A full 4-week technical roadmap in professional Markdown format.",
    agent=architect,
    context=[analysis_task, research_task]
)
        apa_crew = Crew(
    agents=[analyst, researcher, architect],
    tasks=[analysis_task, research_task, roadmap_task],
    process=Process.sequential,
    max_rpm=3,  # Limits the crew to 10 requests per minute
    verbose=True
)

        print("🔥 Kickoff with Groq LLM...")
        result = apa_crew.kickoff()
        final_output = str(result)

        roadmap_id = await save_roadmap(
            user_id=request.user_id,
            github_username=request.github_username,
            roadmap_data=final_output
        )

        return {"status": "success", "roadmap_id": roadmap_id, "data": final_output}

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))