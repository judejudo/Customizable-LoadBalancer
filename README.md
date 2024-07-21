

---

# Customizable Load Balancer

This project is a customizable load balancer built using Flask, Docker, and Docker Compose. The load balancer distributes incoming traffic across multiple Flask servers.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running the Project](#running-the-project)
5. [Testing the Project](#testing-the-project)
6. [Project Structure](#project-structure)
7. [Performance Analysis](#performance-analysis)

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation

Follow these steps to install and set up the project:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/judejudo/Customizable-LoadBalancer.git
    cd Customizable-LoadBalancer
    ```

2. **Create Necessary Directories and Files:**

    Ensure the following directories and files are present in your project structure:

    ```
    Customizable-LoadBalancer/
    ├── docker-compose.yml
    ├── load_balancer/
    │   ├── Dockerfile
    │   ├── __init__.py
    │   ├── load_balancer.py
    │   └── consistent_hashing.py
    ├── server/
    │   ├── Dockerfile
    │   ├── requirements.txt
    │   └── app.py
    ```

3. **Update the `requirements.txt` file:**

    Ensure your `requirements.txt` file in the `server` directory includes all necessary dependencies. An example is shown below:

    ```txt
    Flask==2.0.2
    requests==2.26.0
    ```

## Configuration

Ensure the Dockerfile and docker-compose.yml files are correctly set up:

### Dockerfile for `server` directory

```dockerfile
FROM python:3.12-slim

WORKDIR /server

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
COPY ../load_balancer /app/load_balancer

CMD flask run --host=0.0.0.0 -p 5000
```

### Dockerfile for `load_balancer` directory

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD flask run --host=0.0.0.0 -p 5000
```

### `docker-compose.yml`

```yaml
version: '3.8'

services:
  flask_server1:
    image: flask-server-image1
    build: 
      context: ./server
      dockerfile: Dockerfile
    container_name: flask-server1-container
    ports:
      - "5001:5000"
    restart: on-failure

  flask_server2:
    image: flask-server-image2
    build: 
      context: ./server
      dockerfile: Dockerfile
    container_name: flask-server2-container
    ports:
      - "5002:5000"
    restart: on-failure

  flask_server3:
    image: flask-server-image3
    build: 
      context: ./server
      dockerfile: Dockerfile
    container_name: flask-server3-container
    ports:
      - "5003:5000"
    restart: on-failure

  load_balancer:
    image: load-balancer-image
    build:
      context: ./load_balancer
      dockerfile: Dockerfile
    container_name: load-balancer-container
    ports:
      - "5000:5000"
    restart: on-failure
```

## Running the Project

1. **Build and Start the Containers:**

    Navigate to the root of your project directory (`Customizable-LoadBalancer`) and run the following command:

    ```bash
    docker-compose up --build
    ```

    This command will build the Docker images and start the containers as defined in the `docker-compose.yml` file.

2. **Access the Load Balancer:**

    Once the containers are running, you can access the load balancer via `http://localhost:5000`.

## Testing the Project

To test if the load balancer is working correctly, you can send multiple requests to the load balancer and verify that the requests are being distributed across the Flask servers:

1. **Send Requests:**

    Use a tool like `curl` or Postman to send requests to `http://localhost:5000`.

   
    ```


2. **Verify Load Balancing:**

    Check the logs of the Flask server containers to see if the requests are being distributed among them. You can view the logs using the following command:



## Project Structure

Here's an overview of the project's structure:

```
Customizable-LoadBalancer/
├── docker-compose.yml          # Docker Compose configuration file
├── load_balancer/              # Load balancer directory
│   ├── Dockerfile              # Dockerfile for the load balancer
│   ├── __init__.py             # Makes load_balancer a package
│   ├── load_balancer.py        # Load balancer implementation
│   └── consistent_hashing.py   # Consistent hashing implementation
├── server/                     # Flask server directory
│   ├── Dockerfile              # Dockerfile for the Flask servers
│   ├── requirements.txt        # Python dependencies
│   └── app.py                  # Flask application
```

## Performance Analysis

### Experiment 1: Load Distribution

- Launch 30,000 asynchronous requests on 3 server containers.
- Record the number of requests handled by each server and plot a bar chart.
- Expected Outcome: Even distribution of load among server instances.

![image](https://github.com/user-attachments/assets/73a86595-ecfe-4fda-95b8-f893fe5b98b3)



### Experiment 2: Scalability

- Increment the number of server containers from 2 to 6 (launching 10,000 requests each time).
- Plot a line chart showing the average load of the servers at each run.
- Expected Outcome: Efficient scaling with even load distribution as server instances increase.
![image](https://github.com/user-attachments/assets/154fdbaf-fd7a-4a07-87d8-753e258d4916)


### Experiment 3: Failure Recovery

- Test load balancer endpoints until server failure is achieved.
- Ensure the load balancer spawns new instances to handle the load and maintain the specified number of replicas.
#### Results
![image](https://github.com/user-attachments/assets/528a7c4f-ec09-4b02-b437-a0fee293420f)

<br>
Containers  with the prefix 'emergency_' are spawned on failure of a replica.

- On failure of a server during a test run with 40000 requests, 'emergency_52' and 'emergency_11' were spawned to handle requests

### Experiment 4: Hash Function Modification

- Modified the hash function: i % 512(number) of slots.
- Repeat experiments 1 and 2, analyzing the impact on load distribution and scalability.
- #### Experiment 1 Results:
![image](https://github.com/user-attachments/assets/73a86595-ecfe-4fda-95b8-f893fe5b98b3)
- #### Experiment 2 Results:
![image](https://github.com/user-attachments/assets/154fdbaf-fd7a-4a07-87d8-753e258d4916)


