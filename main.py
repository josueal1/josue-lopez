from flask import Flask, render_template, url_for
from datetime import datetime
from local_db import SOCIAL_LINKS, SERVICES, BLOG_POSTS, VID_RECOMMENDATIONS, NAV_LINKS, LIFE_EVENTS

app = Flask(__name__)

app.config['SECRET_KEY'] = '2e9cddbf90516b76b574b4b2411b43a0'

@app.context_processor
def utility_processor():
	'''The items in the return dict are available within all the templates in the app.'''
	return dict(footer_date=datetime.now(), timeline_events=LIFE_EVENTS)
	

@app.route("/")
@app.route("/about")
def about():
	return render_template("home.html", page_title="About", SOCIAL_LINKS=SOCIAL_LINKS, NAV_LINKS=NAV_LINKS)

@app.route("/services")
def services():
	return render_template("services.html", page_title="Services", SERVICES=SERVICES)

@app.route("/blog")
def blog():
	return render_template("blog.html", page_title="Tech Blog", posts=BLOG_POSTS)

@app.route("/recommendations")
def recommendations():
	return render_template("recommendations.html", page_title="Recommended Learning", recommendations=VID_RECOMMENDATIONS)

@app.route("/portfolio")
def portfolio():
	return render_template("portfolio.html")


if __name__ == "__main__":
	app.run(debug=True)
