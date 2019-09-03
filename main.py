from flask import Flask, render_template, url_for
from datetime import datetime
from local_db import SOCIAL_LINKS, SERVICES, BLOG_POSTS, VID_RECOMMENDATIONS, NAV_LINKS

app = Flask(__name__)

app.config['SECRET_KEY'] = '2e9cddbf90516b76b574b4b2411b43a0'

@app.context_processor
def utility_processor():
	'''A context processor is a function that returns a dictionary. The keys and 
	values of his dictionary are then merged with the template context, for all 
	templates in the app'''
	current_date = datetime.now()
	return dict(footer_date=current_date, python_dir=dir())
	

ROOT_URL = "/"
@app.route(ROOT_URL)
@app.route("/about")
def about():
	return render_template("home.html", page_title="About", SOCIAL_LINKS=SOCIAL_LINKS, NAV_LINKS=NAV_LINKS)

# @app.route("/services")
# def help():
# 	return render_template("services.html", page_title="Services", services=SERVICES)


# @app.route("/contact")
# def contact():
# 	a_contact_form = ContactForm()
# 	return render_template("contact.html", page_title="Contact", form=a_contact_form)

@app.route("/blog")
def blog():
	return render_template("blog.html", page_title="Tech Blog", posts=BLOG_POSTS)

@app.route("/recommendations")
def rec():
	return render_template("recommendations.html", page_title="Recommended Learning", recommendations=VID_RECOMMENDATIONS)


@app.route("/portfolio")
def portfolio():
	return render_template("portfolio.html")


if __name__ == "__main__":
	# app.run(debug=True)
	app.run()

# alternatively, we can use the Unix Command:
# "export FLASK_DEBUG=1" && "flask run"
# in order to achieve debug mode
