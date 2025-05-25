from flask import Flask, render_template, jsonify, request

from query_ai import get_installed_models, get_ai_response

app = Flask(__name__, static_folder='../static', template_folder='../templates')


@app.route('/', methods=['GET'])
def index() -> str:
    """
    The homepage route.
    :return: The render template of the homepage.
    """
    return render_template('index.html')


@app.route('/query-ai', methods=['POST'])
def query_ai():
    """
    The route to handle AI queries.
    :return: A JSON response with the AI's response.
    """
    model = request.form.get('model')
    query = request.form.get('query')
    response = get_ai_response(model, query)
    return jsonify(response=response)


@app.route('/get-models', methods=['GET'])
def get_models():
    """
    Fetch the list of installed models.
    :return: A JSON response containing the list of models.
    """
    models = get_installed_models()
    return jsonify(models=models)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
