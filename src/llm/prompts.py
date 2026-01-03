def get_prompt(context: str, conversation_history: str, query: str):
    """Generate a prompt combining context, history, and query"""

    prompt = f"""Based on the following context and conversation history, 
    please provide a relevant and contextual response. If the answer cannot 
    be derived from the context, only use the conversation history or say 
    "I cannot answer this based on the provided information."
    
    Context from documents:
    {context}

    Previous conversation:
    {conversation_history}

    Human: {query}

    Assistant:"""

    return prompt
