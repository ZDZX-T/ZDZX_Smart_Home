from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def handle_get_request():
    return 'po'


if __name__ == '__main__':
    app.run(debug=False)
