import os
import sys

sys.path.append('..')
from load_balancer.load_balancer import LoadBalancer
# Print the absolute path to the current file (app.py)
print(f"Absolute path to app.py: {os.path.abspath(__file__)}")


if __name__ == '__main__':
    lb = LoadBalancer()
    lb.run()
