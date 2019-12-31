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

NAV_LINKS = [Link("About","/about"),
			 Link("Contact","#contact"),
			 Link("Recommendations","#recommendations"),
			 Link("iPhoneography Portfolio","/portfolio"),
			 Link("Services","/services"),
			 Link("Blog", "/blog")
			]

SERVICES = [
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


BLOG_POSTS = [	{"title": "My First Blog Post", "content": "Because of the proliferation of personal-branding, as sophomore undergrad, I've decided to take-on the world with a keyboard and a screen (plus some wifi). Through this blog, I intend to share life goals, entrepreneural ambitions, and wild visions of tech."}, 
				{"title": "My Second Blog Post", "content": "This is just a test."}
			 ]


VID_RECOMMENDATIONS = ["PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU","PLAE85DE8440AA6B83","PL27BCE863B6A864E3", "PL4cUxeGkcC9gGrbtvASEZSlFEYBnPkmff"]


LIFE_EVENTS = ["Decided to Switch Majors in Software Engineering - Aug 30th 2019"]

TIMELINE_EVENTS = [ Event("April 2017", "Confirmed offer letter from UC Irvine! Zot, Zot! :emoji: "),
					Event("Aug 30th 2019", "Decided to Switch Majors in Software Engineering"),
					Event("July 2017","Flew out to Seattle, WA for Google's Computer Science Summer Institute!"),
					Event("August 2017", "Completed UCI's summer bridge CSSA !")
				  ]
