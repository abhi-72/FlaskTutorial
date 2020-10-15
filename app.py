import flask
from flask import request, jsonify
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True

CORS(app)

# Create some test data for our catalog in the form of a list of dictionaries.
import yaml

with open(r'data.yaml') as f:
    tutorials = yaml.full_load(f)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

def update_yaml(tutorials):
    with open(r'data.yaml', 'w') as f:
        documents = yaml.dump(tutorials, f)

@app.route('/portals', methods=['GET'])
def get_all():
    return jsonify(tutorials)

@app.route('/portals/<int:pk>', methods=['GET'])
def get(pk=None):
    for tutorial in tutorials:
        if tutorial['id'] == pk:
            return jsonify(tutorial)
    return jsonify({'msg':'No tutorial found'})

@app.route('/portals/<int:pk>', methods=['PUT'])
def update(pk=None):
    for tutorial in tutorials:
        if tutorial['id'] == pk:
            tutorial.update(request.json)
    update_yaml(tutorials)
    return jsonify(request.json)

@app.route('/portals', methods=['POST'])
def create():
    data = request.json
    data['id'] = len(tutorials) + 1
    tutorials.append(data)
    update_yaml(tutorials)
    return jsonify(request.json)

app.run()
