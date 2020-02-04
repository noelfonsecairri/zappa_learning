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

@app.route('/notifications', methods=['POST', 'GET'])
def notifications():
	if request.method == 'POST':
		language = request.form.get('language')
		framework = request.form['framework']


		return '''<h1>The language value is: {}</h1>
				<h1>The framework value is {}</h1>'''.format(language, framework)


	return '''<form method="POST">
		Language: <input type="text" name="language"><br>
		Framework: <input type="text" name="framework"><br>
		<input type="submit" value="Submit"><br>
	</form>'''

@app.route('/json_example', methods=['POST'])
def json_example():
	req_data = request.get_json()

	language = req_data['language']
	framework = req_data['framework']
	website = req_data['website']


	return '''<h1>
	The language value is {}.
	The framework value is {}.
	The website value is {}.
	</h1>'''.format(language, framework, website)


if __name__ == "__main__":
	app.run()