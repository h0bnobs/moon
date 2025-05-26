from ollama import Client


def get_ai_response(model: str, query: str, conversation_history: list) -> tuple[str, list]:
    """
    Update the current conversation history and query the AI model using the history and new prompt.
    :param model: The AI model name
    :param query: The user's input/query
    :param conversation_history: List of previous messages
    :return: A tuple containing the AI response and updated conversation history
    """
    conversation_history.append({'role': 'user', 'content': query})
    response = get_client().chat(model=model, messages=conversation_history)
    return response.message.content, conversation_history


def get_installed_models() -> list:
    """
    Get a list of the installed AI models on the host.
    :return: list of installed models.
    """
    s = get_client().list()["models"]
    models = []
    for model in s:
        models.append(model["model"])
    return models


def get_client() -> Client:
    """
    Get an ollama client object.
    :return: An ollama client object.
    """
    return Client(
        host='http://localhost:11434',
        headers={'x-some-header': 'some-value'}
    )
