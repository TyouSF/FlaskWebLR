# Flask 的模板

Flask 中模板的相关使用和介绍

* * *

# 知识点

## Flask 中电子邮件相关的操作

扩展： flask-mail、SendGrid-Python

> Flask-Mail：使用 Flask-Mail 发送电子邮件

-   flask mail 的实例化：`mail = Mail(app)`
-   Flask Mail 的配置
-   构建邮件数据：`message = flask_mail.Message(subject='',recipients=['',''], body='')`
-   发送邮件：`mail.send(message)`

> SendGrid-Python：事务邮件服务 SendGrid

注册并使用 SendGrid 邮件服务提供商，进行事务邮件的发送

## 进阶

-   提供 HTML 正文邮件内容
-   使用 JinJa2 模版组织邮件正文

示例代码：

```Python
from flask import render_template
from flask_mail import Message

def send_subscribe_mail(subject, to, **kwargs):
  message = Message(subject, recipients=[to],sender='flask <%s>' % os.getenv('MAIL_USERNAME'))
  message.body = render_template('emails/subscribe.txt', **kwargs)
  message.html = render_template('emails/subcribe.html', **kwargs)
  mai.send(message)
```
