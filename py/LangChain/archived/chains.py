from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain.prompts import PromptTemplate, ChatPromptTemplate
import os
# def get_chain():
#     llm = OpenAI(temperature=1)
#
#     template = """
#     Extract all privacy-related APIs from the API trace documents using a custom tool that identifies whether a specific class method is a Privacy API. For each identified Privacy API, find its corresponding summary from the summary documents.
#     """
#     prompt_template = ChatPromptTemplate.from_template(template)
#     privacy_api_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="privacy_apis")
#
#     template = """
#     Summarize the UI event flow from the provided UI trace documents in the following format:
#     {   'timestamp': "",
#         'event': 'click/show/etc.',
#         'content': '' }.
#     For the 'content' field, summarize the UI event like what is displayed on the screen or the text of the clicked button."
#     """
#     prompt_template = ChatPromptTemplate.from_template(template)
#     ui_summary_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="ui_summary")
#
#
#     # You are ..., input, first..., second..., your output
#     template = """Analyze issues of inconsistency or conflict and generate a conflict report:
#     Task 1: Identify related Privacy APIs in the API trace (e.g., those with data flow relationships or call dependencies). Compare their summaries to find inconsistencies or conflicts.
#     Task 2: Understand the summaries and compare them against the app’s static information (e.g., reading app property documents, environment information as conditions the app must fulfill) and dynamic information (e.g., API trace, UI trace). The dynamic information should reveal the order of API calls and key information gathered from the UI (such as whether consent dialogs are displayed, whether authorization buttons are clicked, etc.). Analyze whether the app’s use and impact of the APIs align with the requirements in the summaries, and identify any conflicts.
#
#     % Privacy API Summary
#     {privacy_apis}
#
#     % UI summary
#     {ui_summary}
#
#     """
#
#     prompt_template = ChatPromptTemplate.from_template(template)
#     detect_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="ui_summary")
#
#     overall_chain = SimpleSequentialChain(chains=[privacy_api_chain, ui_summary_chain, detect_chain], verbose=True)
#     return overall_chain


def get_chain():
    llm = ChatOpenAI(temperature=0.2, model = "gpt-4o-mini", api_key=os.getenv('OPENAI_API_KEY'))

    template = """
    You are an API Inconsistency Detector.

    I will provide you with the following information:
    1. App Details: Details of the app scraped from Google Play, including description, target audience (content rating), etc.
    2. App Runtime Environment: The environment in which the app is running.
    3. App Runtime Traces: Important events such as UI displays, button clicks, method calls, etc., along with details like displayed/clicked content, stack traces/parameters of called methods, and timestamps of when the events occurred. These events are ordered by timestamp.
    4. Summaries of Privacy APIs: Summaries of privacy APIs called in the trace, including their conditions, effects, and parameter details, extracted from the official developer documentation.
    
    Your task is to:
    
    1. Detect inconsistencies between the observed conditions and effects of API calls in the runtime traces and the conditions and effects described in the API summaries.
    2. Identify dependent privacy APIs from the traces (e.g., APIs with data dependencies or control flow dependencies). Check whether their summaries have inconsistencies or conflicts that could, due to these dependencies, cause potential security or privacy issues.
    
    You should report each inconsistency in the following format. If no inconsistencies are detected, output an empty JSON array: []
    
    [ {{ "involved_APIs": [ {{ "class_name": "class_name", "method_name": "method_name" }} ], "issues": [ {{ "description": "Description of the potential issue", "reason": "Reason why it is an issue", "impact": "Possible consequences it can cause" }} ] }} ]
    
    % App Details
    {app_details}
    
    % Runtime Environment
    {runtime_environment}
    
    % Runtime Traces
    {runtime_traces}
    
    % Summaries of Privacy APIs
    {summaries}
    
    """
    prompt_template = PromptTemplate.from_template(template)
    privacy_api_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="privacy_apis")

    return privacy_api_chain