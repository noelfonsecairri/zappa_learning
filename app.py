from flask import Flask, Response, json, request

app = Flask(__name__)

@app.route('/')
def index():
	return "hello world!", 200

@app.route('/user', methods=['GET'])
def user():
	resp_dict = {"first_name": "Noel", "last_name": "Fonseca"}
	response = Response(json.dumps(resp_dict),200)
	return response

@app.route('/notifications', methods=['POST'])
def notifications():
	req_data = request.get_json()

	language = req_data['language']
	framework = req_data['framework']
	website = req_data['website']
	version_info = req_data['version_info']['python']
	examples = req_data['examples'][0]
	boolean = req_data['boolean']




	return '''<h1>
	The language value is {}.
	The framework value is {}.
	The website value is {}.
	The version info is {}.
	The example at index 0 is {}.
	The boolean value is {}.
	</h1>'''.format(language, framework, website, version_info, examples, boolean)


if __name__ == "__main__":
	app.run()