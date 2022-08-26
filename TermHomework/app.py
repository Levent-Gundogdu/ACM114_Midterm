from flask import Flask, request, render_template
import random

randomGuess = random.randint(1,100)

score = 500

app = Flask(__name__)

@app.route('/')

def my_form():

    return render_template("index.html")

@app.route('/', methods = ['POST'])

def my_form_post():

    global randomGuess

    global score

    msg = ''

    print(score)

    while score > 0:

        myGuess = request.form['myGuess']

        myGuess = int(myGuess)

        if myGuess < randomGuess:
            score = score - 50
            msg = 'Score decreased to '+ str(score) +'. Your number is too low'

            return render_template("index.html", msg = msg)

        elif myGuess > randomGuess:
            score = score - 50
            msg = 'Score decreased to '+ str(score) +'. Your number is too high'

            return render_template("index.html", msg = msg)

        else:

            if myGuess == randomGuess:

                msg = 'Good work! Your final score is: '+ str(score)

                randomGuess = random.randint(1,100)
                score = 500

                return render_template("index.html", msg = msg)

    if score == 0:

        num = 'Your score reached zero. The number I was thinking of was ' + str(randomGuess)

        randomGuess = random.randint(1,100)
        score = 500

        msg = ''

        return render_template("index.html", num = num)

if __name__ == '__main__':

    app.run(debug = True)