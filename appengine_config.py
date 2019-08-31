# it was important to run this file inside AppEngine environment
# because then it understood how to run my app

from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
vendor.add('lib')