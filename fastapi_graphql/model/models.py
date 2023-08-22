# models.py
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class BaseModel(Model):
    id = fields.CharField(  # noqa: A003
        max_length=50,
        pk=True,
        index=True,
        description="id",
        source_field="id",
    )

    def __str__(self):
        return self.name

    class Meta:
        # 抽象类 - 继承 避免代码重写 ,抽象类本身不生成数据表
        abstract = True


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
    account = fields.CharField(max_length=255, index=True, description="账号")
    pwd = fields.CharField(max_length=255, index=True, description="密码")
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


User_orm = pydantic_model_creator(User, name="User")
User_in_orm = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
