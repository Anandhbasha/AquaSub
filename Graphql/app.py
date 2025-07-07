from flask import Flask, request, jsonify
from Schema import schema

app = Flask(__name__)

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    result = schema.execute(
        data.get("query"),
        variables=data.get("variables")
    )
    return jsonify(result.data)

if __name__ == '__main__':
    app.run(debug=True)
