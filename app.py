from flask import Flask, request, Response, json, jsonify
from validate_input import is_valid
from functools import wraps
 
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
def get_http_exception_handler(app):
    """Overrides the default http exception handler to return JSON."""
    handle_http_exception = app.handle_http_exception
    @wraps(handle_http_exception)
    def ret_val(exception):
        exc = handle_http_exception(exception)    
        return jsonify({'code':exc.code, 'message':exc.description}), exc.code
    return ret_val

# Override the HTTP exception handler.
app.handle_http_exception = get_http_exception_handler(app)
    
if __name__ == "__main__":
    #app.debug = True
    app.run()