import jinja2
import os
import webapp2

jinja_environment = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("MyProfile_Templates/Profile_Homepage.html")
        self.response.out.write(template.render())
        print ("Hello world, this is Josue's Blogasaurus !")

class InterestHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("MyProfile_Templates/Interest.html")
        self.response.out.write(template.render())

class FamilyHandler (webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("MyProfile_Templates/Family.html")
        self.response.out.write(template.render())



app = webapp2.WSGIApplication([

('/', MainHandler),
("/Interest", InterestHandler),
("/Family", FamilyHandler)

], debug=True)
