#from google.appengine.ext import vendor
from flask import Flask, render_template, url_for
# from flask_material import Material
from datetime import datetime

#vendor.add("lib")

app = Flask(__name__)
# Material(app)

app.config['SECRET_KEY'] = '2e9cddbf90516b76b574b4b2411b43a0'

posts = [	{"title": "My First Blog Post", "content": "on June 21st, I ran."}, 
			{"title": "My Second Blog Post", "content": "This is just a test."}
		]

services = [
	{ "icon": "perm_contact_calendar",
	  "title":"Web-Development Consultations",
	  "message":"""Have you been wanting to build that website for your small business, software project, or for your CS portfolio? Then let's talk! Throughout my two years, I have specialized in Python and JavaScript web development!""",
	  "href":"/contact",
	  "link_title":"Schedule a Consultation"
	},
	{ "icon" :"developer_mode",
	  "title":"Python, C++, Java Tutorials",
	  "message":"You can spend a millions hours finding the best course of action, but I have curated a list of top three programming YouTube playlist that have helped me succeed as a software developer at UCI!",
	  "href":"/recommendations",
	  "link_title":"Check Them Out!"
	}
]

recommendations = ["PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU","PLAE85DE8440AA6B83","PL27BCE863B6A864E3", "PL4cUxeGkcC9gGrbtvASEZSlFEYBnPkmff"]

@app.context_processor
def utility_processor():
	'''A context processor is a function that returns a dictionary. The keys and 
	values of his dictionary are then merged with the template context, for all 
	templates in the app'''
	current_date = datetime.now()
	return dict(footer_date=current_date, python_dir=dir())
	

ROOT_URL = "/"
@app.route(ROOT_URL)
# @app.route("/about")
def about():
	return render_template("home.html", page_title="About")

# @app.route("/services")
# def help():
# 	return render_template("services.html", page_title="Services", services=services)


# @app.route("/contact")
# def contact():
# 	a_contact_form = ContactForm()
# 	return render_template("contact.html", page_title="Contact", form=a_contact_form)

@app.route("/blog")
def blog():
	return render_template("blog.html", page_title="Tech Blog", posts=posts)

@app.route("/recommendations")
def rec():
	return render_template("recommendations.html", page_title="Recommended Learning", recommendations=recommendations)



if __name__ == "__main__":
	# app.run(debug=True)
	app.run()

# alternatively, we can use the Unix Command:
# "export FLASK_DEBUG=1" && "flask run"
# in order to achieve debug mode
