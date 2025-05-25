from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/', methods=['GET'])
def index() -> str:
    """
    The route for the port scanning settings page.
    :return: The render template of the port scanning settings html file.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=80)