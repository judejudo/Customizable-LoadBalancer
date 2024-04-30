FROM python:3.12-slim

WORKDIR /server

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Modify the CMD to include --host=0.0.0.0
CMD flask run --host=0.0.0.0 -p 5000