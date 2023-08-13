# doc-search
AI-powered chatbot that analyzes your personal documents.

## Running
Run `python3 doc-search.py` in the CLI to run with OpenAI gpt-3.5-turbo model. Include `open` as a command line argument to run with open source model.
Currently only supports HuggingFaceHub models, and it doesn't work very well. Working on that.

## API Keys
Add API keys in a `constants.py` file in the root directory in the following format:

OPENAI_KEY = "YOUR OPENAI API KEY"<br>
SERPAPI_KEY = "YOUR SERPAPI API KEY"<br>
HUGGINGFACEHUB_KEY = "YOUR HUGGINGFACE HUB KEY"<br>
PINECONE_KEY = "YOUR PINECONE KEY"

SERPAPI_KEY and at least one of OPENAI_KEY and HUGGINGFACEHUB_KEY are required for the application to work.<br>
PINECONE_KEY is optional. If not provided, the application will store embeddings locally in FAISS vector database. Note that the application will only work with a Pinecone index named `langchain1` (will update this later).

OpenAI: https://platform.openai.com/account/api-keys<br>
SerpAPI: https://serpapi.com/manage-api-key<br>
Huggingface: https://huggingface.co/settings/tokens<br>
Pinecone: https://www.pinecone.io/<br>

## Loading Data
If you're storing embeddings locally, the application will automatically load all pdf files from the `data` directory.<br>
If you're using Pinecone to store vector embeddings, include `load` as a command line argument to load all pdf files from the `data` directory. Otherwise, the application will just read from existing data in the Pinecone index.