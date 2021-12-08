FROM python:3.9-slim
RUN apt-get update
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
