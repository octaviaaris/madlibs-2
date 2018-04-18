"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

ANIMALS = ['giraffe', 'hippo', 'ostrich', 'monkey', 'flamingo', 'parrot']


MADLIBS = ['madlib.html', 'madlib2.html']


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """ Shows madlib form """

    answer = request.args.get("answer")

    if answer == "no":
        return render_template("goodbye.html")
    elif answer == "yes":
        animals = sample(ANIMALS, 3)
        return render_template("game.html", animals=animals)

# function that chooses random madlib to render
# return html to be put into show_madlib view function

@app.route('/' + madlib[:-5])
def show_madlib():

    person_value = request.args.get("person")
    color_value = request.args.get("color")
    noun_value = request.args.get("noun")
    adjective_value = request.args.get("adj")
    animal_value = request.args.get("animal")
    place_value = request.args.get("place")
    food_value = request.args.get("food")
    sound_value = request.args.get("sound")
    action_value = request.args.get("action")
    mood_value = request.args.get("mood")

    madlib = choice(MADLIBS)

    return render_template(madlib,
                           person=person_value,
                           color=color_value,
                           noun=noun_value,
                           adjective=adjective_value,
                           animal=animal_value,
                           place=place_value,
                           food=food_value,
                           sound=sound_value,
                           action=action_value,
                           mood=mood_value)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
