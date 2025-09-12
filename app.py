from flask import Flask
from App.Utilities.Url import Url

app = Flask(__name__)

@app.route("/")
def index():
    return {
        "current_url": Url.base_url()
    }

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
