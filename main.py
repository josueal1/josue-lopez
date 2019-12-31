from flask import Flask, render_template, url_for
from datetime import datetime
from local_db import SOCIAL_LINKS, BLOG_POSTS, VID_RECOMMENDATIONS, NAV_LINKS, LIFE_EVENTS

app = Flask(__name__)

app.config['SECRET_KEY'] = '2e9cddbf90516b76b574b4b2411b43a0'

@app.context_processor
def utility_processor():
	'''The items in the return dict are available within all the templates in the app.'''
	return dict(footer_date=datetime.now(), timeline_events=LIFE_EVENTS, NAV_LINKS=NAV_LINKS)

@app.route("/")
def about():
	return render_template("home.html", page_title="About", SOCIAL_LINKS=SOCIAL_LINKS, NAV_LINKS=NAV_LINKS)

@app.route("/contact")
def contact():
	return render_template("contact.html", page_title="Contact | Services")

@app.route("/blog")
def blog():
	return render_template("blog.html", page_title="Tech Blog", posts=BLOG_POSTS)

@app.route("/recommendations")
def recommendations():
	return render_template("recommendations.html", page_title="Recommended Learning", recommendations=VID_RECOMMENDATIONS)

@app.route("/portfolio")
def portfolio():
	return render_template("portfolio.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 40

if __name__ == "__main__":
	app.run(debug=True)
