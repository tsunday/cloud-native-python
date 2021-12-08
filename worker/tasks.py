from time import sleep

from worker import app


@app.task
def calculate():
    print("Calculation has started")
    sleep(10)
    print("Calculation done!")
    return
