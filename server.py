from flask import Flask, request,render_template
from flask_restful import Api, Resource


import random
import math

# Taking Inputs
lower = 1
 
# Taking Inputs
upper = 10
 
# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ",
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")
 
# Initializing the number of guesses.
count = 1

 
# for calculation of minimum number of
# guesses depends upon range
"""
while count < math.log(upper - lower + 1, 2):
    count += 1
 
    # taking guessing number as input
    guess = int(input("Guess a number:- "))
 
    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count - 1, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
"""

 
# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
# Create a Flask object and an Api object.
app = Flask(__name__)
"""
    if request.method == 'POST':
        guess = request.form['guess']
        if guess == x:
            return "Congratulations!"
        else:
            count+=1
            remainingGuesses = 3-count
            if(count > 3):
                return "Game Over. The number was: " + x
            else:
                return "try again"
    """
"""
            <div>Try Again :( {remainingGuesses} guesses remaining!</div>
            <form method="post">
            <input type="text" name = "guess"/>
            <input type="submit" name = "submit"/>
            </form>"""#.format(remainingGuesses=remainingGuesses)
@app.route("/")
def newHome():
    return render_template("game.html")


# Start the applictaion.
if __name__ == '__main__':
    app.run(host='0.0.0.0')
