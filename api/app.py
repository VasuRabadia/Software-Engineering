# python requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/add/<x>/<y>", methods=["GET"])
def add_nubers(x, y):
    return jsonify({"result": float(x) + float(y)})


if __name__ == "__main__":
    app.run(debug=True)
