# doc-search
AI-powered chatbot that analyzes your personal documents.

## Running
Run `python3 doc-search.py` in the CLI to run with OpenAI gpt-3.5-turbo model. Run `python3 doc-search.py open` to run with open source model.
Currently only supports HuggingFaceHub models, and it doesn't work very well. Working on that.

## API Keys
Add API keys in a `constants.py` file in the root directory in the following format:

OPENAI_KEY = "YOUR OPENAI API KEY"<br>
SERPAPI_KEY = "YOUR SERPAPI API KEY"

OpenAI: https://platform.openai.com/account/api-keys<br>
SerpAPI: https://serpapi.com/manage-api-key
