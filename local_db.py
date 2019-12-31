class Link:
	def __init__(self, name, href):
		self.href = href
		self.name = name

class Event:
	def __init__(self, date, detail):
		self.date = date
		self.detail = detail

SOCIAL_LINKS = [Link("LinkedIn","https://www.linkedin.com/in/josue-a-lopez/"),
				Link("Github", "https://github.com/josueal1"),
				Link("Instagram", "https://www.instagram.com/joshh__17"),
				Link("Twitter", "https://www.twitter.com/galvez2j")
		 	   ]

NAV_LINKS = [Link("About","/"),
			 Link("Blog", "/blog"),
			 Link("Timeline","/Timeline"),
			 Link("Gallery","/portfolio"),
			 Link("Contact","/contact"),
			]

BLOG_POSTS = [	{"title": "My First Blog Post", "content": "Because of the proliferation of personal-branding, as sophomore undergrad, I've decided to take-on the world with a keyboard and a screen (plus some wifi). Through this blog, I intend to share life goals, entrepreneural ambitions, and wild visions of tech."}, 
				{"title": "My Second Blog Post", "content": "This is just a test."}
			 ]

VID_RECOMMENDATIONS = ["PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU","PLAE85DE8440AA6B83","PL27BCE863B6A864E3", "PL4cUxeGkcC9gGrbtvASEZSlFEYBnPkmff"]

LIFE_EVENTS = [ Event("April 2017", "Confirmed offer letter from UC Irvine! Zot, Zot! :emoji: "),
					Event("July 2017","Flew out to Seattle, WA for Google's Computer Science Summer Institute!"),
					Event("August 2017", "Completed UCI's summer bridge CSSA !"),
					Event("August 2019", "Switched major from CS to Software Engineering")
				  ]
