# pythonAPI
- Using Flask
- API Endpoint to sum values of a JSON data input
- Takes the sum of two variables (x and y) inputted in a JSON and returns it via an HTTP Post.
- Validates input data, returns error if input does not have the right input fields or values are not a number.

## Test the API Endpoint with curl:
- curl -X POST https://lyft-tech-sample.herokuapp.com/test --data '{"x": 4, "y": 2}' -H 'Content-Type: application/json'
