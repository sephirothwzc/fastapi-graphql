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
# 设置环境变量
$ poetry add python-dotenv
# 增加设置类型约束
$ poetry add pydantic-settings

```

- 设置制表符使用空格缩进采用4个空格 settings.json 设置 保证注释的生成

```json
{
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter"
    },
    "python.formatting.provider": "none",
    "editor.detectIndentation": false,
    "editor.tabSize": 4,
}
```

- 数据迁移方案 aerich

```python
TORTOISE_ORM = {
    "connections": {"default": settings.orm_db_url},
    "apps": {
        "models": {
            "models": ["fastapi_graphql.model.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
```

```shell
# 根据配置init
$ aerich init -t fastapi_graphql.config.env_setting.TORTOISE_ORM
# 生成sql（执行一次）
$ aerich init-db 
# 差分sql（）
$ aerich migrate
# 升级到最新版本（执行）
$ aerich upgrade
# 显示历史记录
$ aerich history
# 降级
$ aerich downgrade
```

- tortoise-orm log

```py
import logging
import sys

@app.on_event("startup")
async def startup_event():
    """添加在应用程序启动之前运行初始化数据库"""
    await init()
    fmt = logging.Formatter(
        fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    sh = logging.StreamHandler(sys.stdout)
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(fmt)

    # will print debug sql
    logger_db_client = logging.getLogger("tortoise.db_client")
    logger_db_client.setLevel(logging.DEBUG)
    logger_db_client.addHandler(sh)
```

- gql create model input

```python
class User(BaseModel):
    """
    用户表

    Args:
        Model (_type_): _description_

    Returns:
        _type_: _description_
    """

    table = "user"
    name = fields.CharField(max_length=255, index=True, description="用户名")
    account = fields.CharField(max_length=255, description="账号")
    pwd = fields.CharField(max_length=255, description="密码", null=True)
    collect = fields.TextField(null=True, default="[]", description="用户收藏")
    table_description = "用户表"

    def __str__(self):
        return self.name

    class PydanticMeta:
        exclude = ["pwd"]

    def to_dict(self, pwd=True):  # 这个方法自定义的时候使用
        data = {i: getattr(self, i) for i in self.__dict__ if not i.startswith("_")}
        if pwd:
            del data["pwd"]  # 不返回密码
        return data


User_orm = pydantic_model_creator(User, name="UserOrm")
User_in_orm = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)


@strawberry.experimental.pydantic.input(model=User_in_orm, all_fields=True)
class UserInput:
    pass


@strawberry.experimental.pydantic.type(model=User_orm, all_fields=True)
class UserType:
    pass
```

```python
from dataclasses import asdict

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_user(self, user: UserInput) -> Optional[UserType]:
        user_dict = asdict(user)
        result = await User.create(**user_dict)
        return await User_orm.from_tortoise_orm(result)

```
