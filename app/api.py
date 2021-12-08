from flask import Flask, Response

from worker.tasks import calculate

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return "Hello world!"


@app.route("/jobs/", methods=["POST"])
def create_job():
    calculate.delay()
    return Response(status=201)
