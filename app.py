from flask import Flask, jsonify
from queries import get_all_players

app = Flask(__name__)

@app.route("/players")
def players():

    return jsonify(get_all_players())

if __name__ == "__main__":
    app.run(debug=True)
