from flask import Flask, render_template, jsonify, request, session, g
from query_ai import get_installed_models, get_ai_response
from flask_session import Session

app = Flask(__name__, static_folder='../static', template_folder='../templates')
app.secret_key = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.before_request
def clear_session_on_first_request():
    if not session.get('session_cleared', False):
        session.clear()
        session['session_cleared'] = True


@app.route('/', methods=['GET'])
def index() -> str:
    return render_template('homepage.html')


@app.route('/query-ai', methods=['POST'])
def query_ai():
    model = request.form.get('model')
    query = request.form.get('query')
    history = session.get('history', [])
    response, updated_history = get_ai_response(model, query, history)
    session['history'] = updated_history
    return jsonify(response=response)


@app.route('/get-models', methods=['GET'])
def get_models():
    models = get_installed_models()
    return jsonify(models=models)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
