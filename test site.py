
#Flask is class and flask is framework

from flask import Flask, render_template

#variable to store Flask class instance
#render_template access HTML file, stores in the python App file and displays it on the URL

app=Flask(__name__)

# / is home page
@app.route('/')
def home():
	return render_template("home.html")

#functions cannot have same name i.e. home, about funcs

@app.route('/aboutme/')
def about():
	return render_template("about.html")

if __name__=="__main__":
	app.run(debug=True)

# you don't have to close whenever you make changes to the web app script.If the script is running it automatically refreshes.
