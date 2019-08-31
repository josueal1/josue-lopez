# Delete old folder on App Engine terminal

# Clone the new folder from Github

# sudo pip install -r requirements -t lib

# gcloud init

# gcloud app deploy

from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
vendor.add('lib')
