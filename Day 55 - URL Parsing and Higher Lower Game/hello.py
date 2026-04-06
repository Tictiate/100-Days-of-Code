from flask import Flask
app = Flask(__name__)

def make_bold(function):
    text = function()
    return f"<b>{text}</b>"

def make_emphasis(function):
    text = function()
    return f"<em>{text}</em>"

def make_underlined(function):
    text = function()
    return f"<u>{text}</u>"

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def bye():
    return "Bye!"

@app.route("/username/<name>")  # Angled brackets means username
def greet(name):
    return f"Hello {name}!"

# to take path as input to variable use <path:varname>

if __name__ == "__main__":
    app.run(debug=True)