import os
from crewai import Agent, LLM
from crewai.tools import tool # Import the tool decorator
from tools.rag_query import query_tech_trends
from langchain_community.tools import DuckDuckGoSearchRun

# 1. Initialize the raw LangChain tool
search = DuckDuckGoSearchRun()

# 2. Wrap it in the CrewAI @tool decorator to satisfy the BaseTool requirement
@tool("duckduckgo_search")
def search_tool(query: str):
    """
    Search the internet for the latest tech trends and industry news 
    when the local database does not have sufficient information.
    """
    return search.run(query)

# 3. Define the LLM
groq_llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7
)

def get_researcher_agent():
    return Agent(
        role='Tech Trend Researcher',
        goal='Find trends using the internal vector database and web search.',
        backstory="""You are a specialist researcher who relies on 'trend_researcher' 
        for company data and 'duckduckgo_search' for the live web.""",
        tools=[query_tech_trends, search_tool], # Now both are valid BaseTool instances
        llm=groq_llm,
        verbose=True,
        allow_delegation=False
    )