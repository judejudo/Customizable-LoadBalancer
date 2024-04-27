from flask import Flask
from uhashring import HashRing
import os
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Define your server instances
servers = [
    "server1",
    "server2",
    "server3"
]

# Initialize the hash ring with server instances
hash_ring = HashRing(servers)

@app.route('/home', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    key = "key"  # You can use any key you want for consistent hashing
    server_id = get_server_id(key)
    logging.info(f"Request for key '{key}' served from server: {server_id}")
    return f'Hello from Server: {server_id}\n'


@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    # Sends empty response with a valid response code (200 OK)
    return '', 200

def get_server_id():
    # Get server ID based on consistent hashing with load balancing
    key = "key"  # You can use any key you want for consistent hashing
    server_id = hash_ring.get_node(key)
    return server_id

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
