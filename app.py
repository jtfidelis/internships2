from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/about')
def about():
    return "This is the about page"


if __name__ == "__main__":
    app.run()