from flask import Flask, request
import http
import urllib3

app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def index():
    print(request)
    return "hello flask", 200


@app.route('/read',methods=['POST', 'GET'])
def read():
    print(request)
    x = dummyFuncForMock()
    return "hello read api " + x, 200

@app.route('/readnew',methods=['POST', 'GET'])
def readnew():
    http_pool = urllib3.poolmanager
    http_pool.PoolManager().request(method='post',data = [])
    

    print(request)
    x = dummyFuncForMock()
    return "hello read api " + x, 200



def dummyFuncForMock():
    return "1"

if __name__ == "__main__":
    app.run(host='0.0.0.0')