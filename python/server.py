from flask import Flask
from flask import request
from flask import Response
from flask import jsonify
from flask import make_response

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hi There!</h1>"

@app.route('/sayHello', methods=['POST'])
def sayHello():
    person_json = request.get_json()
    person_name = person_json['name']
    return 'Hello '+person_name

@app.route('/eval', methods=['POST'])
def eval():
    resp_body = {}

    if 'Q1' in request.form.keys():
        ans = request.form['Q1']
        resp_body['Q1'] = {}
        if ans == 'A1':
            resp_body['Q1'][ans] = True
        else:
            resp_body['Q1'][ans] = False

    if 'Q2' in request.form.keys():
        ans = request.form['Q2']
        resp_body['Q2'] = {}
        if ans == 'A3':
            resp_body['Q2'][ans] = True
        else:
            resp_body['Q2'][ans] = False

    if 'Q3' in request.form.keys():
        ans = request.form['Q3']
        resp_body['Q3'] = {}
        if ans == 'A2':
            resp_body['Q3'][ans] = True
        else:
            resp_body['Q3'][ans] = False

    if 'Q4' in request.form.keys():
        ans = request.form['Q4']
        resp_body['Q4'] = {}
        if ans == 'A4':
            resp_body['Q4'][ans] = True
        else:
            resp_body['Q4'][ans] = False

    if 'Q5' in request.form.keys():
        ans = request.form['Q5']
        resp_body['Q5'] = {}
        if ans == 'A1':
            resp_body['Q5'][ans] = True
        else:
            resp_body['Q5'][ans] = False

    print('Response: ', resp_body)
    resp = make_response(jsonify(resp_body), 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'application/json'

    return resp

app.run()
