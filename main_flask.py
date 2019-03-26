from flask import Flask
from flask import render_template

app = Flask(__name__)

ROOT_URL = "/"
@app.route(ROOT_URL)
def index():
	response = render_template("index.html")
	return response


if __name__ == "__main__":
	app.run()