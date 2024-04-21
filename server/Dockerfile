FROM python:3.11.5

WORKDIR /server

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD python app.py