import logging
from flask import Flask

app = Flask(__name__)
wsgi_app = app.wsgi_app

# Configure logging to show WARNING and above
logging.basicConfig(level=logging.WARNING)
app.logger.setLevel(logging.WARNING)

import FlaskExercise.views