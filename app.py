from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to Flask App!"

# Example API route
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "name": "Flask App",
        "status": "running"
    }
    return jsonify(data)

# POST route example
@app.route('/api/add', methods=['POST'])
def add_numbers():
    data = request.json
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)

    result = num1 + num2
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
