from flask import Flask
from flask import request

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

app.run()

