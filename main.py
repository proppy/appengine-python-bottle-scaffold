"""`main` is the top-level module for your Bottle application."""

# Import the Bottle framework
from bottle import Bottle

# Create the Bottle wsgi application.
bottle = Bottle()


# Handle requests to '/'.
@bottle.route('/')
def home():
    """ Return Hello World at application root URL"""
    return "Hello World"


# Handle 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.'

# App Engine Python runtime will take care of serving the WSGI application.
# (no need to call `bottle.run()`).
