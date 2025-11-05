from flask import Flask

app = Flask(__name__)


@app.route('/hello-world', methods=['GET'])
def hello_world():
    return 'Hello world!\n', 418

# Start server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
