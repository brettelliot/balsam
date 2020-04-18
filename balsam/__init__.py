import os

from flask import Flask

app = Flask(__name__)

# Load our flask config from class.
configurations = {
    "development": "balsam.config.DefaultConfig",
}
app.config.from_object(configurations[os.getenv("FLASK_ENV")])

import balsam.views
