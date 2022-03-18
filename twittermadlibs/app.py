# save this as app.py
from flask import Flask
from .__main__ import main

app = Flask(__name__)


@app.route("/")
def hello():
    return main()


if __name__ == "__main__":
    app.run()
