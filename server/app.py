from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def return_server_id():
    response = jsonify({
        "message" : "Hello from Server: [ID]", "status" : "successful"
    })
    return response

@app.route('/hearbeat', methods=['GET'])
def heartbeat():
    return '', 200

if __name__ == "__main__":
    app.run()