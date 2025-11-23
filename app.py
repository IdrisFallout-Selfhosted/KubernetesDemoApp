from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Kubernetes Demo App1!'

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200


if __name__ == '__main__':
    app.run()
