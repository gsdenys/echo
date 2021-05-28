from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def home(path):
    if request.method == 'GET' or request.method == 'DELETE':
        all_args = request.args
        return jsonify(all_args)
    else:
        data = request.json
        return jsonify(data)

if __name__ == "__main__":
	app.run()
