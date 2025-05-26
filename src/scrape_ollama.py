import requests
import re


def get_family_names() -> list:
    """
    Fetches family names of AI models from the Ollama library.
    :return: List of family names of AI models.
    """
    content = requests.get('https://ollama.com/library?sort=popular').content.decode('utf-8').splitlines()
    family_names = []
    for i in range(len(content)):
        if 'li x-test-model' in content[i]:
            family_names.append(content[i + 1].split('"')[1].split('/')[2])
    return family_names


def get_model_names_and_sizes(family_names: list) -> dict:
    """
    Fetches model names and sizes from the Ollama library for each family.

    :param family_names: List of family names to fetch models for.
    :return: Dictionary with model names as keys and their sizes as values.
    """
    model_names_and_sizes = {}
    for family in family_names:
        content = requests.get(f'https://ollama.com/library/{family}').content.decode('utf-8').splitlines()
        for i in range(len(content)):
            if content[i].strip().startswith(
                    f'<a href="/library/{family}:') and 'block group-hover:underline text-sm font-medium text-neutral-800' in \
                    content[i].strip():
                match = re.search(r'>(.*?)</a>', content[i].strip())
                if match:
                    model_name = match.group(1)
                for j in range(15, 18):
                    if 'GB' in content[i + j].strip() or 'MB' in content[i + j].strip():
                        match = re.search(r'>(.*?)</p>', content[i + j].strip())
                        if match:
                            model_names_and_sizes[model_name] = match.group(1)
    return model_names_and_sizes
