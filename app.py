from flask import Flask, request
from flask.json import jsonify
from werkzeug.exceptions import BadRequest
from werkzeug.utils import escape
from fregservice import FregService
from flask import Response

app = Flask(__name__)

# powershell: 
# $env:FLASK_APP = path
# flask run

@app.route("/", methods=["GET"])
def root():
    if request.method == "GET":
        return escape("This is the root :)")

@app.route("/person/<personnummer>", methods=['GET'])
def person(personnummer):
    if request.method == 'GET':
        if personnummer is not None:
            personnummer = str(personnummer)+".json"
        try:
            person = FregService(file_name=personnummer)
            return jsonify(person.batch)
        except Exception as e:
            response = e.description
            return Response(response, e.code)

    
if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)
    
