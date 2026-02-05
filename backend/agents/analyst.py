from tools.github_api import get_github_user_data
from crewai import Agent,LLM

import os
groq_llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7,
    max_tokens=1024
)
def get_analyst_agent():
    return Agent(
        role='GitHub Technical Analyst',
        goal='Analyze the user\'s GitHub repositories to identify their core tech stack and skill level.',
        backstory="""You are an expert technical recruiter and developer advocate. 
        You excel at looking at codebases and understanding a developer's 'Technical DNA'—
        what they are good at and where they are in their journey.""",
        tools=[get_github_user_data],
        verbose=True,
        llm=groq_llm, # Switched to Groq  # Explicitly set this to the cheaper model
        allow_delegation=False
    )