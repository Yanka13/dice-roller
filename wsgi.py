from flask import Flask, jsonify
import random 

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"roll": random.randint(1,6)})


if __name__ == "__main__":
    app.run(debug=True, port=8000)
    
    