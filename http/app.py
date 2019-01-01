"""
    :author: Tyou
"""

import os
try:
    from urlparse import urlparse, urljoin
except ImportError:
    from urllib.parse import urlparse, urljoin

from jinja2 import escape
from jinja2.utils import generate_lorem_ipsum
from flask import Flask, make_response, request, redirect, url_for, abort, session, jsonify


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')


# 通过 request 请求对象，从查询字符串 args 和 cookies 中获取 name
@app.route('/')
@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'name 的默认值')
    response = '<h1>hello, %s</h1>' % escape(name)  # 使用 escape 来避免 XSS 的攻击
    if 'logged_in' in session:
        response += '[Authenticated]'
    else:
        response += '[Not Authenticated]'
    return response


# 通过 Flask 中的 redirect 实现重定向
@app.route('/hi')
def hi():
    return redirect(url_for('hello'))


# Flask 中 URL 规则的转换器使用示例 int
@app.route('/goback/<int:year>')
def go_back(year):
    return 'Welcome to %d' % (2018 - year)


# Flask 中 URL 规则的转换器使用示例 any
@app.route('/colors/<any(blue, white, red):color>')
def thress_colors(color):
    return '<p>Love is patient and kind. Love is not jealous or boastful or pround or rude.</p>'


# 返回错误的响应示例，使用 abort 方法
@app.route('/brew/<drink>')
def teapot(drink):
    if drink == 'coffee':
        abort(418)
    else:
        return 'A drop of tea'


# 404 使用 abort
@app.route('/404')
def not_found():
    abort(404)


# Flask 返回不同数据类型的响应
@app.route('/note', defaults={'content_type': 'text'})
@app.route('/note/<content_type>')
def note(content_type):
    content_type = content_type.lower()
    if content_type == 'text':
        body = '''Note
to: Peter
from: Jane
heading: Reminder
body: Don't forget the party!
'''
        response = make_response(body)  # 使用 make_respone 创建响应对象
        response.mimetype = 'text/plain'  # 使用响应对象的 mimetype 属性定义响应主体数据类型
    elif content_type == 'html':
        body = '''<!DOCTYPE html>
<html>
<head></head>
<body>
  <h1>Note</h1>
  <p>to: Peter</p>
  <p>from: Jane</p>
  <p>heading: Reminder</p>
  <p>body: <strong>Don't forget the party!</strong></p>
</body>
</html>
'''
        response = make_response(body)
        response.mimetype = 'text/html'
    elif content_type == 'xml':
        body = '''<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Peter</to>
  <from>Jane</from>
  <heading>Reminder</heading>
  <body>Don't forget the party!</body>
</note>
'''
        response = make_response(body)
        response.mimetype = 'application/xml'
    elif content_type == 'json':
        body = {"note": {
            "to": "Peter",
            "from": "Jane",
            "heading": "Remider",
            "body": "Don't forget the party!"
        }
        }
        response = jsonify(body)  # 使用 Flask 的 jsonify 方法构造 json 类型数据的响应主体
    else:
        abort(404)
    return response


# Flask 中设置 cookie
@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)  # 使用响应对象的 set_cookie 方法设置 cookie
    return response


# 使用 session 认证登陆，即： 通过认证的用户，向 session 中添加字段
# Flask 中使用 session 需要设置 SECRET_KEY 加密密钥
@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('hello'))


# 模拟需权限认证才能访问的视图/URL
@app.route('/admin')
def admin():
    if 'logged_in' not in session:
        abort(403)
    return 'Welcome to admin page'


# 模拟注销用户登陆 即：从 session 中删除认证字段
@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('hello'))


# AJAX 模拟示例
@app.route('/post')
def show_post():
    post_body = generate_lorem_ipsum(n=2)
    return '''
    <h1>A very long post</h1>
    <div class="body">%s</div>
    <button id="load">Load More</button>
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script type="text/javascript">
    $(function() {
        $('#load').click(function() {
            $.ajax({
                url: '/more',
                type: 'get',
                success: function(data){
                    $('.body').append(data);
                }
            })
        })
    })
    </script>
    ''' % post_body


@app.route('/more')
def load_post():
    '''
    AJAX 异步请求的地址
    '''
    return generate_lorem_ipsum(n=1)


# 重定向回上一页
# 需要注意开放重定向的漏洞，对重定向进行校验
@app.route('/foo')
def foo():
    return '<h1>Foo page</h1><a href="%s">Do something and redirect</a>' \
           % url_for('do_something', next=request.full_path)


@app.route('/bar')
def bar():
    return '<h1>Bar page</h1><a href="%s">Do something and redirect</a>' \
           % url_for('do_something', next=request.full_path)


@app.route('/do-something')
def do_something():
    # 此处为本函数将来所需执行的内容
    return redirect_back()


def is_safe_url(target):
    '''
    校验重定向页面的安全性：
    1. 获取程序内部请求的 host_url
    2. 使用 urljoin 将程序自身的 host_url 与目标页相对 url 进行拼接为绝对 url 地址
    3. 使用 urlparse 进行 1 和 2 中的主机地址和路径等进行解析
    4. 确保主机地址相同，为程序内部的 url 地址
    '''
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
        ref_url.netloc == test_url.netloc


def redirect_back(default='hello', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target=target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))
