from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return (
        "Hello, Cloud Run! Auto Deploy with Cloud Build and Cloud Source Repositories!"
    )
