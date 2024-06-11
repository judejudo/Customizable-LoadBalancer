from flask import Flask, jsonify, request
from .consistent_hashing import ConsistentHashMap

class LoadBalancer:
    def __init__(self):
        self.app = Flask(__name__)
        self.consistent_hash_map = ConsistentHashMap(num_slots=512)
        self.replicas = set()  # Set to store the names of managed server replicas

        @self.app.route('/home', methods=['GET'])
        def home():
            server_id = self.consistent_hash_map.map_request_to_server(request_id=123456)
            return f"Hello from Server {server_id}!"

        @self.app.route('/heartbeat', methods=['GET'])
        def heartbeat():
            return '', 200

        @self.app.route('/rep', methods=['GET'])
        def get_replicas():
            return jsonify({
                "message": {
                    "N": len(self.replicas),
                    "replicas": list(self.replicas)
                },
                "status": "successful"
            }), 200

        @self.app.route('/add', methods=['POST'])
        def add_replicas():
            data = request.json
            if 'n' not in data or 'hostnames' not in data:
                return jsonify({"error": "Invalid request. 'n' and 'hostnames' are required."}), 400
            num_new_replicas = data['n']
            hostnames = data['hostnames']
            if num_new_replicas != len(hostnames):
                return jsonify({"error": "Number of hostnames should match 'n'."}), 400
            self.replicas.update(hostnames)
            return jsonify({
                "message": {
                    "N": len(self.replicas),
                    "replicas": list(self.replicas)
                },
                "status": "successful"
            }), 200

        @self.app.route('/rm', methods=['DELETE'])
        def remove_replicas():
            data = request.json
            if 'n' not in data or 'hostnames' not in data:
                return jsonify({"error": "Invalid request. 'n' and 'hostnames' are required."}), 400
            num_remove_replicas = data['n']
            hostnames = data['hostnames']
            if num_remove_replicas != len(hostnames):
                return jsonify({"error": "Number of hostnames should match 'n'."}), 400
            self.replicas.difference_update(hostnames)
            return '', 204

    def run(self):
        self.app.run(debug=True, host='0.0.0.0', port=5000)
