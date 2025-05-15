from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, Flask! First start local server."


@app.route('/contact')
def contact():
    return "Contact page"


@app.route('/about')
def about():
    return "About page"


@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}"


if __name__ == "__main__":
    app.run(debug=True)
