"""Flask application views."""
from . import app


@app.route('/', methods=['GET'])
def root():
    return '''<b>Balsam root loaded</b>'''
