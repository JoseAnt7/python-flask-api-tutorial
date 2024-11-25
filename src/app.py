from flask import Flask, jsonify, request

todos = [{"label": "My first task", "done": False}]

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200  

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json  
    print("Incoming request with the following body", request_body)

    if "label" in request_body and "done" in request_body:
        todos.append(request_body) 
        return jsonify(todos), 200
    else:
        return jsonify({"error": "Invalid todo format. Keys 'label' and 'done' are required."}), 400
    
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)

    if 0 <= position < len(todos):
        todos.pop(position)  
        return jsonify(todos), 200 
    else:
        return jsonify({"error": "Position out of range"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
