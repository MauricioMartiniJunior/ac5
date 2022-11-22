import os
from flask_cors import CORS
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)
CORS(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/api/rota', methods=['POST'])
def rota():

    json = request.get_json()
    firstName = json['txtNome']
    return jsonify(first_name=firstName.upper())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
