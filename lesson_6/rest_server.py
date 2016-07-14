from flask import Flask
from flask import request
import json
__author__ = 'sekely'

app = Flask('my_app')
users = {}


@app.route('/')
def hello_world():
    return 'hello world!\n'


@app.route('/<first_name>/<last_name>')
def say_my_name(first_name, last_name):
    return 'hello %s %s!\n' % (first_name, last_name)


@app.route('/user')
def user():
    first_name = request.args.get('name')
    last_name = request.args.get('last_name')
    phone_number = request.args.get('number')
    return 'hello %s %s!\nyour phone number is %s\n' % (first_name, last_name, phone_number)


@app.route('/user_account', methods=['POST', 'GET'])
def user_account():
    first_name = request.values.get('name')
    last_name = request.values.get('last_name')
    phone_number = request.values.get('number')
    code = '%s%s' % (first_name, last_name)
    if request.method == 'POST':
        users[code] = [first_name, last_name, phone_number]
        return 'registered %s\n' % users[code]
    elif request.method == 'GET':
        user = users.get(code)
        if user:
            return '%s %s phone number is %s\n' % tuple(user)
        else:
            return json.dumps(list(users.values()))


if __name__ == '__main__':
    app.run()
