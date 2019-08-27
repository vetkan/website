
#Flask is class and flask is framework

from flask import Flask

#variable to store Flask class instance

app=Flask(__name__)

# / is home page
@app.route('/')

def home():
	return "Website content goes here"

if __name__=="__main__":
	app.run(debug=True)
