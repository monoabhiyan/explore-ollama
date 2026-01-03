from ollama import chat, ChatResponse

from llm.prompts import get_prompt


def generate_response(query: str, context: str, conversation_history: str = ""):
    """Generate a response using AI model with conversation history"""

    prompt = get_prompt(context, conversation_history, query)

    try:
        response: ChatResponse = chat(
            model="deepseek-r1:8b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that answers questions based on the provided context.",
                },
                {"role": "user", "content": prompt},
            ],
        )

        return response.message.content
    except Exception as e:
        return f"Error generating response: {str(e)}"
