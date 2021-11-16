from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request

# Khởi tạo Flask Server Backend
app = Flask(__name__)

# Apply Flask CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/getdata", methods=['POST'] )
def printdata():
    data = request.form.get("data");
    return  "<p>"+data+" </p>";


@app.route('/minus', methods=['POST','GET'] )
@cross_origin(origin='*')
def minus_process():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    kq = a - b
    return 'Kết quả là: ' + str(kq)

# Start Backend
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='6868')