import os
import warnings

warnings.filterwarnings("ignore")
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages.ai import AIMessage

# Load environment variables from .env file
load_dotenv()

tavily_search = os.getenv("tavily_api_key")
groq_api = os.getenv("groq_api_key")

# Initialize Groq API
groq = ChatGroq(
    models="llama-3.3-70b-versatile",
    api_key=groq_api,
)

# Setup the agents
from langgraph.prebuilt import create_react_agent


def get_reponse_from_model(model_id, model_provider, allow_search, prompt, query):
    # Select model provider
    if model_provider == "Groq":
        llm = ChatGroq(model=model_id)  # Initialize Groq model
    else:
        llm = ChatGroq(model=model_id)  # If needed, other providers can be handled here

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    # Create agent
    agents = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=prompt
    )

    state = {"messages": [{"role": "user", "content": str(query)}]}
    result = agents.invoke(state)
    messages = result.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]

    return ai_messages[-1]  # Return the last AI message


if __name__ == "__main__":
    # Testing purpose
    model = "Groq"  # Use the initialized groq object
    model_id = "llama-3.3-70b-versatile"
    prompts = "act like a smart AI assistant"  # Instructions for the AI
    allow_search = True  # Allow or disallow search functionality
    query = "provide me the best history along with their explanation and link, that should be about AI"

    try:
        response = get_reponse_from_model(model_provider=model, model_id=model_id, prompt=prompts, allow_search=allow_search,query=query)
        print(response)
    except Exception as e:
        print(f"Error: {e}")
