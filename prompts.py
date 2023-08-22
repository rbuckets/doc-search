DOCSEARCH_DESCRIPTION = """
Searches through the papers for information regarding the prompt.
"""

SEARCH_DESCRIPTION = """
A search engine. Used when you need to look up outside information not provided in the papers. Input should be a search query. Don't use this tool unless it's absolutely necessary.
"""

AGENT_PROMPT_PREFIX = """
Have a conversation with a human, answering it's questions about papers. You have access to the following tools:
"""

AGENT_PROMPT_SUFFIX = """
Gather information found in the papers using the search_papers tool. Always search through the papers first. Only if you desperately need it, look up additional information using the search tool. Begin!"

{chat_history}
Question: {input}
{agent_scratchpad}
"""