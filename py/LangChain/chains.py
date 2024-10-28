from langchain.llms import OpenAI
from langchain import LLMChain
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chains import SimpleSequentialChain

def get_chain():
    llm = OpenAI(temperature=1)

    template = """
    Extract all privacy-related APIs from the API trace documents using a custom tool that identifies whether a specific class method is a Privacy API. For each identified Privacy API, find its corresponding summary from the summary documents.    
    """
    prompt_template = ChatPromptTemplate.from_template(template)
    privacy_api_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="privacy_apis")

    template = """
    Summarize the UI event flow from the provided UI trace documents in the following format: 
    {   'timestamp': "", 
        'event': 'click/show/etc.', 
        'content': '' }. 
    For the 'content' field, summarize the UI event like what is displayed on the screen or the text of the clicked button."
    """
    prompt_template = ChatPromptTemplate.from_template(template)
    ui_summary_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="ui_summary")


    # You are ..., input, first..., second..., your output
    template = """Analyze issues of inconsistency or conflict and generate a conflict report:
    Task 1: Identify related Privacy APIs in the API trace (e.g., those with data flow relationships or call dependencies). Compare their summaries to find inconsistencies or conflicts.
    Task 2: Understand the summaries and compare them against the app’s static information (e.g., reading app property documents, environment information as conditions the app must fulfill) and dynamic information (e.g., API trace, UI trace). The dynamic information should reveal the order of API calls and key information gathered from the UI (such as whether consent dialogs are displayed, whether authorization buttons are clicked, etc.). Analyze whether the app’s use and impact of the APIs align with the requirements in the summaries, and identify any conflicts.
    
    % Privacy API Summary
    {privacy_apis}
    
    % UI summary
    {ui_summary}
    
    """

    prompt_template = ChatPromptTemplate.from_template(template)
    detect_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="ui_summary")

    overall_chain = SimpleSequentialChain(chains=[privacy_api_chain, ui_summary_chain, detect_chain], verbose=True)
    return overall_chain