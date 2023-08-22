# 开发手册

|日期|人员|版本|说明|
|----|----|----|----|
|2023-08-21|吴占超|v0.1|

## 编码规范

- 文件全小写下划线分词命名

### 安装手册

- 传统模式 已过时不推荐

```shell
# 创建目录
$ mkdir python-fastapi-graphql
$ cd python-fastapi-graphql
# 虚拟环境
$ python3 -m venv jitenv
# 激活
$ source jitenv/bin/activate
# vscode 打开
$ code .
# 在虚拟环境中安装 FastAPI
$ pip3 install fastapi
# 安装 Uvicorn 服务器 
$ pip3 install "uvicorn[standard]"
# 创建main.py form fastapi import FastApi 报错，重启 vscode即可
$ touch main.py
# 点击运行和调试 创建launch文件选择fastapi->点击运行即可(断点调试) or uvicorn main:app --reload
$ uvicorn main:app --reload
# 安装 Mysql ORM
$ pip3 install 'tortoise-orm[asyncmy]'
# 依赖包及其版本信息
$ pip3 freeze > requirements.txt
# 生成依赖
$ pip3 install -r requirements.txt
```

- Poetry 模式

```shell
# 安装poetry
$ brew install poetry
# or 
$ brew install --build-from-source poetry
# 创建项目 --src单独目录 可以取消 $  poetry new --src python-fastapi-graphql
$ poetry new fastapi-graphql
# 目录跳转
$ cd fastapi-graphql
# vscode 打开
$ code .
# git
$ git init
# 使用 Poetry 的虚拟环境 or poetry env use .3.9
$ poetry env list
# 激活虚拟环境
$ poetry shell
# 声明你的依赖
$ poetry install
# 创建requirements.txt自poetry.lock 暂时不需要
$ poetry export --output requirements.txt
# 安装包
$ poetry add fastapi "uvicorn[standard]"
# 格式化 black='*' 开发环境配置
$ poetry add black='*' --dev
# * linting with ruff (目前无法使用 只能用 pip3 install ruff)
$ poetry add ruff='*' --dev  
# 运行 (创建 main.py)
$ uvicorn fastapi_graphql.main:app --reload    
# 模型类
$ poetry add pydantic
# pre-commit hooks
$ poetry add pre-commit --dev
# * commitizen 目前有问题不能使用
$ poetry add commitizen --dev
# pre-commit install 激活.git hooks 创建文件 .pre-commit-config.yaml
$ pre-commit install
# 扩展 安装 brew install pyenv 设置 全局python 版本
# 数据库orm
$ poetry add "tortoise-orm[asyncmy]"
```
