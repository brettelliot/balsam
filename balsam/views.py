"""Flask application views."""
from . import app
from flask import jsonify


@app.route('/', methods=['GET'])
def root():
    return '''<b>Balsam root loaded</b>'''

@app.route('/balsam/api/v1/tests/simple-object', methods=['GET'])
def simple_object():
    obj = {'string_member': 'string value', 'int_member': 2}
    return jsonify(obj)
