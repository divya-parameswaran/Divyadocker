from flask import Flask
app = Flask(__name__)

@app.route('/')
def question():
    return '<h2>What is Docker?</h2>'

@app.route('/divyadocker')
def answer():
	return '<p> A Docker is an open-source software for developing, shipping, and running applications. </p>'
if __name__ == '__main__':	
	app.run(host="0.0.0.0", debug=True)
