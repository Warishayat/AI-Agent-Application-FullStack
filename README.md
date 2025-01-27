# AI-Agent Full-Stack Application

This is a full-stack application that allows you to interact with AI agents through a web interface. The application provides users the ability to define AI agents with custom system prompts, choose from various available models, and make web queries. It integrates multiple AI model providers and tools for dynamic interactions.

## Features

- **Custom AI Agent Configuration**: Define your own system prompt to customize how the AI behaves.
- **Multiple Model Providers**: Choose from a variety of AI models, including Groq and Gemini, for different use cases.
- **Web Search Integration**: Allows AI agents to fetch data from the web based on user queries.
- **Interactive Web UI**: Build, modify, and interact with your AI agents using a user-friendly Streamlit interface.

## Tech Stack

- **Backend**: Python, FastAPI (optional if you want to extend with an API)
- **Frontend**: Streamlit
- **AI Providers**: Groq, Gemini
- **AI Tools**: Tavily Search (for web search integration)
- **Libraries**: LangChain, LangGraph

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher
- `pip` for installing dependencies

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Warishayat/AI-Agent-Application-FullStack.git
   cd AI-Agent-Application-FullStack
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # For macOS/Linux
   .venv\Scripts\activate      # For Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory of the project.
   - Add the necessary API keys and other configurations:
     ```
     groq_api_key=your_groq_api_key
     tavily_api_key=your_tavily_api_key
     ```

5. Run the Streamlit app:
   ```bash
   streamlit run Frontend.py
   ```

   This will start the application locally at `http://localhost:8501`.

## Usage

1. Define your custom system prompt in the "Define your AI-Agents here" text area.
2. Choose the model provider (Groq or Gemini).
3. Select the model from the available options.
4. Enable or disable web search.
5. Enter a query and click "Search" to interact with the AI agent.

The app will return a response from the selected AI model based on the query and system prompt.

## Contributing

If you would like to contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
