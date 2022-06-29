from flask import Flask, request,render_template, redirect, url_for
from flask_restful import Api, Resource


import random
import math

# Taking Inputs
lower = 1
 
# Taking Inputs
upper = 10

x = random.randint(lower, upper)





app = Flask(__name__)

            
@app.route("/home")
def home():
    x = random.randint(lower, upper)
    return render_template("game.html", number = x)
countG = 1
@app.route("/guess", methods = ["GET", "POST"])
def guess():
    if request.method == "POST":
        currGuess = request.form["guess"]
        
        if int(currGuess) == x:
            return redirect(url_for('win'))
        else:
            countG += 1
            
            return redirect(url_for('tryagain'))
        
    return render_template("guessScreen.html")

@app.route("/tryagain")
def tryagain():
    return render_template("tryagain.html", guesses = 3-countG)

@app.route("/win")
def win():
    return render_template("winScreen.html")
# Start the applictaion.
if __name__ == '__main__':
    app.run(host='0.0.0.0')
