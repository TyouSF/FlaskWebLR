# Flask 表单处理

Flask 中对于表单的处理和使用（扩展：flask-wtf）

* * *

# 知识点

主要应用到如下几个库：

-   WTForms：python 编写的一个表单库
-   Flask-WTF：flask 中基于 WTForms 编写的扩展库
-   Flask-CKEditor：flask 中富文本编辑库

## 字段类

WTForms 中字段类与对应的 HTML 标签转化，诸如：

BooleanField、DateField、FileField、PasswordField 等

## 处理表单数据

-   客户端验证
-   服务端验证

## 自定义验证器

WTForms 中自定义编写验证器

-   行内验证器
-   全局验证器

# 其他场景解决方案

-   单个表单，多个提交按钮，来处理不同逻辑
-   单页面单视图处理多表单处理
-   多视图处理多表单
-   多文件上传以及单文件上传
