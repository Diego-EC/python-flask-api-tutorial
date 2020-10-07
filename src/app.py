from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_todos = jsonify(todos)
    print("get_todos")
    return json_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append({"label": decoded_object["label"], "done": decoded_object["done"]})
    json_todos = jsonify(todos)
    return json_todos

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    json_todos = jsonify(todos)
    return json_todos

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)