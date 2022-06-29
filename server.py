from itertools import count
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
   
    return render_template("game.html", number = x)
countG = 0
@app.route("/guess", methods = ["GET", "POST"])
def guess():
    if request.method == "POST":
        currGuess = request.form["guess"]
        
        if int(currGuess) == x:
            return redirect(url_for('end', message = "win"))
        else:
            global countG
            countG = countG + 1
            return redirect(url_for('tryagain'))
        
    return render_template("guessScreen.html")

@app.route("/tryagain")
def tryagain():
    global countG
    if 3-countG == 0:
        return redirect(url_for('end', message = "loss"))
    return render_template("tryagain.html", guesses = 3-countG)

@app.route("/end/<message>")
def end(message):
    global x
    x = random.randint(lower, upper)
    return render_template("winScreen.html",message = message,number = x)
# Start the applictaion.
if __name__ == '__main__':
    app.run(host='0.0.0.0')
