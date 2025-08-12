SUMMARIZER_SYSTEM_PROMPT = """
You are a summarizer for a task.

You will be given a task and a list of tools.
User query:
{user_query}

Memory:
{memory}


Summarize the user query based on the memory.
"""
