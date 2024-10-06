from flask import Flask, request, jsonify
from query_data import qandr
from flask_cors import CORS


app = Flask(__name__)
CORS(app) 
@app.route("/api/query", methods=["POST"])
def query():
    print("hiiii")
    query = request.json["query"]
    print("Query received: ", query)
    response = qandr(query)
    
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)