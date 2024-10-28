from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.tools import BaseTool
from langchain.llms import OpenAI
from langchain import LLMMathChain, SerpAPIWrapper
from tools import privacy_api_checker
from chains import get_chain
from loaders import load_api_trace, load_ui_trace, load_picture, load_api_summary
def get_agent():
    llm = OpenAI(temperature=0)

    search = SerpAPIWrapper()
    chain = get_chain()
    tools = [
        Tool(
            name = "Privacy API Checker",
            func=privacy_api_checker.run,
            description="Given a class name and a method name, check whether it is a privacy API"
        ),

        Tool(
            name="Search",
            func=search.run,
            description="useful for when you need to know something you don't know"
        ),
        Tool(
            name="chain",
            func=chain.run,
            description="Follow the chain when you are running"
        )

    ]

    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    return agent


