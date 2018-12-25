# -*- coding: utf-8 -*-

"""
    :author: Tyou
"""

from flask import Flask


app = Flask(__name__)


# 最小的 flask 程序
@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'


# 同一个视图绑定多个 URL
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>say Hello Flask!</h1>'


#  添加 URL 变量
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name
