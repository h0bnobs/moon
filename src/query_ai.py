from ollama import chat
from ollama import ChatResponse
from ollama import Client

# assuming the ai is running on localhost:11434
# base_url = "http://192.168.5.228:11434/api/chat"
def get_ai_response(model: str, query: str) -> str:
    client = Client(
        host='http://192.168.5.228:11434',
        headers={'x-some-header': 'some-value'}
    )
    response = client.chat(model=model, messages=[
        {
            'role': 'user',
            'content': query,
        },
    ])
    if isinstance(response, ChatResponse):
        return response.message.content
    else:
        return 'something went wrong.'

def get_installed_models() -> list:
    client = Client(
        host='http://192.168.5.228:11434',
        headers={'x-some-header': 'some-value'}
    )
    s = client.list()["models"]
    models = []
    for model in s:
        models.append(model["model"])
    return models

# wow all hail https://github.com/ollama/ollama-python

#print(response['message']['content'])