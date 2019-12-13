from flask import Flask, Response, json

app = Flask(__name__)

@app.route('/')
def index():
	return "hello world!", 200

@app.route('/user', methods=['GET'])
def user():
	resp_dict = {"first_name": "John", "last_name": "Doe"}
	response = Response(json.dumps(resp_dict),200)
	return response

if __name__ == "__main__":
	app.run()