class ConsistentHashMap:
    def __init__(self, num_slots):
        self.num_slots = num_slots
        self.hash_map = [None] * num_slots

    def hash_function_request(self, request_id):
        return (request_id + 2 * request_id + 17) % self.num_slots

    def hash_function_virtual_server(self, server_id, replica_id):
        return (server_id + replica_id + 2 * replica_id + 25) % self.num_slots

    def add_virtual_server(self, server_id):
        for replica_id in range(self.num_slots):
            slot = self.hash_function_virtual_server(server_id, replica_id)
            original_slot = slot  # Keep track of the original slot for checking loop completion
            while self.hash_map[slot] is not None:
                slot = (slot + 1) % self.num_slots
            # Apply linear probing in case of collision
             
            # Break if we've looped through all slots without finding an empty one
                if slot == original_slot:
                    break
                
        # If an empty slot is found, add the virtual server
            if self.hash_map[slot] is None:
                self.hash_map[slot] = server_id
            
    # Add virtual servers for each server container
    
     

        
    # Add virtual servers for each server container
    


    def map_request_to_server(self, request_id):
        slot = self.hash_function_request(request_id)
        while self.hash_map[slot] is None:
            # Apply linear probing in case of empty slot
            slot = (slot + 1) % self.num_slots
        return self.hash_map[slot]

    def handle_server_failure(self, server_id):
        # Remove all instances of the failed server from the hash map
        for i in range(self.num_slots):
            if self.hash_map[i] == server_id:
                self.hash_map[i] = None

# Example usage
num_slots = 512
consistent_hash_map = ConsistentHashMap(num_slots)

# Add virtual servers for each server container
num_server_containers = 3
for server_id in range(num_server_containers):
    consistent_hash_map.add_virtual_server(server_id)

# Map requests to server containers
request_id = 123456
server_id = consistent_hash_map.map_request_to_server(request_id)
print(f"Request {request_id} mapped to Server {server_id}")

# Handle server failure
failed_server_id = 1
consistent_hash_map.handle_server_failure(failed_server_id)
