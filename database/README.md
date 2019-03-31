# Flask 数据库的使用

Flask 中数据库的操作，以及数据模型等的范例

* * *

# 知识点

## SQLAlchemy 对数据库的支持，以及 Flask-SQLAlchemy 扩展的应用

-   Flask 中 flask-sqlalchemy 的实例：`db = SQLAlchemy(app)`
-   对于数据库的链接操作
-   数据模型的定义：`class dbmodel(db.Model)`
-   flask-sqlalchemy 中字段的定义：`id = db.Column(db.Integer, primary_key)`
-   数据库的操作：CRUD（create：增加/创建；Read：读取/查询；Update：更新/更改；Delete：删除）
-   Python Shell 上下文的注册和使用：
    ```Python
    @app.shell_context_processor
    def make_shell_context():
      return dict(db=db, Note=Note)
    ```
-   flask-sqlalchemy 中一对多，多对多等关联关系的操作和使用

## flask-migrate 迁移数据库的使用

-   迁移环境的实例化：`migrate = Migrate(app, db)`
-   Migrate 命令生成迁移脚本：`flask db migrate -m 'some notes...'`
-   使用 upgrade 子命令更新数据库：`flask db upgrade`

## 进阶操作

-   级联操作
-   事件监听
