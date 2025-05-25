from ollama import chat
from ollama import ChatResponse
from ollama import Client

conversation_history = []


def get_ai_response(model: str, query: str) -> str:
    global conversation_history

    # Add the user's query to the conversation history
    conversation_history.append({'role': 'user', 'content': query})

    client = Client(
        host='http://localhost:11434',
        headers={'x-some-header': 'some-value'}
    )
    response = client.chat(model=model, messages=conversation_history)

    if isinstance(response, ChatResponse):
        # Add the AI's response to the conversation history
        conversation_history.append({'role': 'assistant', 'content': response.message.content})
        return response.message.content
    else:
        return 'Something went wrong.'


def get_installed_models() -> list:
    client = Client(
        host='http://localhost:11434',
        headers={'x-some-header': 'some-value'}
    )
    s = client.list()["models"]
    models = []
    for model in s:
        models.append(model["model"])
    return models

# wow all hail https://github.com/ollama/ollama-python

# print(response['message']['content'])
