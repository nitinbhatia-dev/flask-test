from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def index():
    print(request)
    return "hello flask", 200


@app.route('/read',methods=['POST', 'GET'])
def read():
    print(request)
    return "hello read api", 200



if __name__ == "__main__":
    app.run(host='0.0.0.0')