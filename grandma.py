from flask import Flask, request, redirect
import twilio.twiml
import random

app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
}

WEATHER = [
    'Are you wearing a jacket?',
    'Sweetie, it\'s so chilly',
    'Do you need an umbrella?',
    'Are you wearing a hat?',
]

QUESTIONS = [
    'Do you have a girlfriend/boyfriend?',
    'Are you eating enough?',
    'Do you have a job yet?',
    'Where do you live again?',
    'Do you have any friends?',
    'Sweetie, what do you think of the fall of American democracy?',
    'When are you going to graduate?',
    'Are you coming to the church potluck on Saturday?',
]

RESPONSES = [
    'That\'s so nice',
    'You should call more',
    'That\'s nice dear',
    'Next time you visit we can make pies together',
    'You look so frail all the time',
]

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""

    from_body = request.values.get('Body', None).lower()
    if from_body == 'hi grandma':
        message = 'ayyy'
    else:
        message = random.choice(QUESTIONS + RESPONSES)

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
