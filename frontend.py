import streamlit as st
from Agents import get_reponse_from_model  # Import the function from agents.py
import os

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

# Initialize the API key and other environment variables
tavily_search = os.getenv("tavily_api_key")
groq_api = os.getenv("groq_api_key")

# Set up the Streamlit page configuration
st.set_page_config(page_title="AI-AGENT Application", layout="centered")
st.title("AI-AGENT APPLICATION")
st.write("Create and interact with AI-AGENTS")

# Text area to define the system prompt
system_prompt = st.text_area("Define your AI-Agent here", height=70, placeholder="Type your system prompt here")

# List of available models
Available_Models = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768", "gemma2-9b-it", "llama3-70b-8192",
                    "llama3-8b-8192"]

# Radio button for selecting the model provider
provide = st.radio("Choose Provider", ("Groq","Gemini"))
provider = "Groq"
# Select model based on provider
if provider == "Groq":
    selected_model = st.selectbox("Choose Model", Available_Models)

# Checkbox to allow web search
allow_web_search = st.checkbox("Allow Web Search")

# Text area for the user query
query = st.text_area("Enter your query to Search", height=150, placeholder="Type your Query here")

# When the "Search" button is clicked
if st.button("Search"):
    if query.strip():
        # Directly call the agent function
        try:
            # Get the response from the AI agent
            response = get_reponse_from_model(
                model_id=selected_model,
                model_provider="Groq",
                allow_search=allow_web_search,
                prompt=system_prompt,
                query=query
            )

            # Display the result from the agent
            st.subheader("Response from AI-Agent:")
            st.write(response)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a query before clicking Search.")
