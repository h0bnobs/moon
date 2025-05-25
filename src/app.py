from flask import Flask, render_template, jsonify

from query_ai import get_installed_models

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index() -> str:
    """
    The homepage route.
    :return: The render template of the homepage.
    """
    return render_template('index.html')
@app.route('/query-ai', methods=['POST'])
def query_ai() -> str:
    """
    The route to handle AI queries.
    :return: The render template of the AI query page.
    """

    return render_template('index.html')

@app.route('/get-models', methods=['GET'])
def get_models():
    """
    Fetch the list of installed models.
    :return: A JSON response containing the list of models.
    """
    models = get_installed_models()
    return jsonify(models=models)

if __name__ == "__main__":
    app.run(debug=True, port=80)