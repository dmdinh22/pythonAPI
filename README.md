# pythonAPI
- Using Flask
- API Endpoint to sum values of a JSON data input
- Takes the sum of two variables (x and y) inputted in a JSON and returns it via an HTTP Post.
- Validates input data, returns error if input does not have the right input fields or values are not a number.
- Currently input validation method checks for "x" and "y" inputs and that the values are numbers. 
- Input fields can be added or changed within valida_input.py

## Test the API Endpoint with curl:
- curl -X POST https://lyft-tech-sample.herokuapp.com/test --data '{"x": 4, "y": 2}' -H 'Content-Type: application/json'
