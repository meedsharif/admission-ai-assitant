# Flask app

from flask import Flask,send_from_directory, request, jsonify
from flask_cors import CORS

from chat import chat

app = Flask(__name__)
CORS(app)

@app.post('/ask')
def ask_question():
    payload = request.json
    question = payload.get("question", "")
    response = chat(question)

    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(debug=True)