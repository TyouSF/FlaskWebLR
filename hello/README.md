# hello

Flask 基本形式

* * *

# 知识点

1.  `pipenv`  管理项目虚拟环境

    -   使用 pip 安装包，安装 pipenv
    -   在所需的项目根目录下，使用 `pipenv install` 给项目配置虚拟环境
        -   `pipenv -h` 可查看命令帮助信息，如下为常用命令：
        -   `pipenv --venv` 查看虚拟环境的路径  
        -   `pipenv --rm` 删除当前项目的虚拟环境
        -   `pipenv install [PackageName]` 项目在虚拟环境中安装所需的依赖
        -   `pipenv shell`  激活虚拟环境
        -   `exit` 退出虚拟环境

2.  `python-dotenv` 管理 Flask 项目环境变量的配置

    -   `pipenv install python-dotenv` 虚拟环境中安装
    -   项目根目录中创建如下两个配置文件：
        -   `.env`  用于存储敏感的配置，项目提交时该文件默认需忽略
        -   `.flaskenv` 用于存储 flask 相关的变量配置，多为研发/测试环境

3.  `watchdog` 监控文件变动

    替换 flask 默认的 Werkzeug 中 stat 重载器

    -   `pipenv install watchdog --dev`   安装该包

    pipenv 中使用 `--dev` 表示将该依赖声明为开发依赖，在 pipfile 中会被添加到 dev-packages 中

    如果需要在创建运行环境时，一并安装开发依赖的库，可以在创建环境的命令中添加 '--dev' 参数，即 `pipenv install --dev`

4.  `flask shell` 启动 python shell

    使用 flask shell 来启动 python shell，而不直接启动单独的 python shell 环境

    flask shell 启动的交互式环境中，会**自动包含 flask 程序上下文**环境，且 flask app 的实例也会被直接导入，方便直接使用
