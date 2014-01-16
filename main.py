"""`main` is the top-level module for your Bottle application."""

# Import the Bottle framework.
from bottle import Bottle
# Import the App Engine Users API.
from google.appengine.api import users

# Create the Bottle wsgi application.
bottle = Bottle()


# Handle HTTP requests to '/'.
@bottle.route('/')
def home():
    """ Return a personalized greeting."""
    user = users.get_current_user()
    return "Hello %s!" % (user or "World")

# Handle HTTP 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.'

# App Engine Python runtime will take care of serving the WSGI application.
# (no need to call `bottle.run()`).
