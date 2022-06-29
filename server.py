from flask import Flask, request,render_template, redirect, url_for
from flask_restful import Api, Resource


import random
import math

# Taking Inputs
lower = 1
 
# Taking Inputs
upper = 10

x = random.randint(lower, upper)

count = 1



app = Flask(__name__)

            
@app.route("/home")
def home():
    return render_template("game.html",number = x)

@app.route("/guess", methods = ["GET", "POST"])
def guess():
    if request.method == "POST":
        currGuess = request.form["guess"]
        print(currGuess)
        if currGuess == x:
            return redirect(url_for('win'))
        return currGuess
    return render_template("guessScreen.html")

@app.route("/win")
def win():
    return render_template("winScreen.html")
# Start the applictaion.
if __name__ == '__main__':
    app.run(host='0.0.0.0')
