from flask import Flask, request,render_template
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

            
@app.route("/")
def newHome():
    return render_template("game.html",number = x)


# Start the applictaion.
if __name__ == '__main__':
    app.run(host='0.0.0.0')
