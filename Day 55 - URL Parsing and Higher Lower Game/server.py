import random
from flask import Flask
app = Flask(__name__)

ans = random.randint(0, 9)

def lower():
    return ('<h1 style= "color: red">Too Low, Try Again!</h1>'
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')

def higher():
    return ('<h1 style= "color: violet">Too High, Try Again!</h1>'
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')

def correct():
    return ('<h1 style = "color: green">You Found Me!</h1>'
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')

@app.route('/')
def home():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')

@app.route('/<int:number>')
def page(number):
    if number < ans:
        return lower()
    elif number == ans:
        return correct()
    else:
        return higher()


if __name__ == "__main__":
    app.run(port=5001)