from flask import Flask, request, Response, json, jsonify
from validate_input import is_valid
from werkzeug.exceptions import HTTPException
 
app = Flask(__name__)
 
@app.route('/')
def index():
	return 'Hello Lyft!'

@app.route("/test", methods = ["POST"])
def api_message():
    # ensure that we received a JSON object
    if request.is_json:
        # set data var to json request object
        data = request.json
        #validate input values
        if is_valid(data):
            # build a new object
            total_dict = {}
            #set value to "sum" key
            total_dict["sum"] = sum(data.values())
            #encode to json
            json_data = json.dumps(total_dict)
            # return json object
            return json_data


@app.errorhandler(Exception)
# error handling class
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    # return json object with error
    return jsonify(error=str(e)), code

if __name__ == "__main__":
    from werkzeug.exceptions import default_exceptions
    for ex in default_exceptions:
        app.register_error_handler(ex, handle_error)
    #app.debug = True
    app.run()