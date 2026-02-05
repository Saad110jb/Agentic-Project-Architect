from crewai import Agent,LLM

import os
groq_llm = LLM(
    model="groq/llama-3.1-8b-instant",    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7,
    max_tokens=1024
)
def get_architect_agent():
    return Agent(
        role='Senior Project Architect',
        goal='Create a detailed 4-week project roadmap including tech stack, weekly goals, and a final project name.',
        backstory="""You are a Senior Architect at a top-tier tech firm. 
        You take raw research and skill assessments and turn them into clear, 
        step-by-step execution plans that a developer can follow to build something impressive.""",
        verbose=True,
        llm=groq_llm, # Switched to Groq  # Explicitly set this to the cheaper model
allow_delegation=False  # <--- THIS MUST BE FALSE
    )   