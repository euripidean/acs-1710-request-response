"""
Request Response App
"""
import random
from flask import Flask


app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?!'

@app.route('/madlib/<adjective>/<noun>')
def madlib(adjective,noun):
    """Display a madlib story based on the user input."""
    return f'There once was a {adjective} {noun} who was scared of heights.\n To help rid them of their fear, their other {noun} friends decided to book a surpise sky diving trip!'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Multiply two numbers"""
    if number1.isdigit() and number2.isdigit():
        number1 = int(number1)
        number2 = int(number2)
        total =  number1 * number2
        return f'{number1} times {number2} is {total}'
    else:
        return 'Invalid input. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """Repeats string n number of times"""
    new_string = ""
    if not word.isnumeric() and n.isdigit():
        n = int(n)
        for n in range(n):
            new_string += word + " "
        return f'{new_string}'
    else:
        return 'Invalid input. Please try again by entering a word and a number!'

@app.route('/dicegame')
def dicegame():
    """Random game of chance"""
    roll = random.randint(1,6)
    if roll == 6:
        return 'You rolled a 6. You won!'
    else:
        return f'You rolled a {roll}. You lost!'

#RUN SERVER
if __name__ == '__main__':
    app.run(debug=True)
