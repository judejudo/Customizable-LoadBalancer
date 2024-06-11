# <<<<<<< master
import os
import sys
# =======
from flask import Flask
from uhashring import HashRing
import os
import logging

logging.basicConfig(level=logging.INFO)
# >>>>>>> master

sys.path.append('..')
from load_balancer.load_balancer import LoadBalancer
# Print the absolute path to the current file (app.py)
print(f"Absolute path to app.py: {os.path.abspath(__file__)}")

# <<<<<<< master

# if __name__ == '__main__':
#     lb = LoadBalancer()
#     lb.run()
# =======
#Define route for home endpoint
@app.route('/home', methods=['GET'])
def home():
    #Get server Id from environment variable or set it to unknown if not found
    server_id = os.environ.get('SERVER_ID', 'Unknown')
    return f'Hello from Server: {server_id}\n'

#Define route for heartbeat endpoint
@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    # Sends empty response with a valid response code (200 OK)
    return '', 200

if __name__ == '__main__':
    #Run the application on all available network intefaces, port 5000
    app.run(host='0.0.0.0', port=5000)
# >>>>>>> master
