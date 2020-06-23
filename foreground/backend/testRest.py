#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from flask import jsonify

app = Flask(__name__)


@app.route('/test', methods=['GET', 'POST','PUT'])
def get_args():
    if request.method == 'GET':
        print(request.args)
        return 'you send server a GET request'
    elif request.method == 'POST':
        res = request.json
        print(res['price'])
        # print(request.form)
        # print(request.values)
        return "you send server a POST request"
    elif request.method == 'PUT':
        res = request.json
        print(res['price'])
        # print(request.form)
        # print(request.values)
        return "you send server a POST request"

if __name__ == '__main__':
    app.debug = True
    app.run()
