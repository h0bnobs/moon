from ollama import chat
from ollama import ChatResponse
from ollama import Client

# assuming the ai is running on localhost:11434
# base_url = "http://192.168.5.228:11434/api/chat"
def get_ai_response() -> str:
    client = Client(
        host='http://192.168.5.228:11434',
        headers={'x-some-header': 'some-value'}
    )
    response = client.chat(model='deepseek-r1:1.5b', messages=[
        {
            'role': 'user',
            'content': 'Why is the sky blue?',
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
    print(client.list()["models"])
    return client.list()["models"]

# wow all hail https://github.com/ollama/ollama-python
get_ai_response()

#print(response['message']['content'])