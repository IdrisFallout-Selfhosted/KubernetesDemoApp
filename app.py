from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Kubernetes Demo App1!'


if __name__ == '__main__':
    app.run()
