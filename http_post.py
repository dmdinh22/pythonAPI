from flask import Flask, request, Response, json, jsonify
 
app = Flask(__name__)
 
@app.route("/test", methods = ["POST"])
def api_message():
    try:
        if request.is_json:
            # set data var to json request object
            data = request.json
            # build a new object
            total_dict = {}
            #set value to "sum" key
            total_dict["sum"] = sum(data.values())
            #encode to json
            json_data = json.dumps(total_dict)
            # return json object
            return json_data
        else:
            return "Invalid JSON data"
    except (TypeError, NameError):
        print("There was an error with your JSON input, please try again.")
        
if __name__ == "__main__":
    app.debug = True
    app.run()