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
    created_at = fields.DatetimeField(auto_now_add=True, description="创建时间")
    created_id = fields.CharField(max_length=50, description="创建人")
    updated_at = fields.DatetimeField(auto_now=True, description="修改时间")
    updated_id = fields.CharField(max_length=50, description="更新人")
    business_code = fields.CharField(max_length=255, description="业务编码")
    db_version = fields.IntField(default=1, description="数据版本")

    def __str__(self):
        return self.name

    class Meta:
        # 抽象类 - 继承 避免代码重写 ,抽象类本身不生成数据表
        abstract = True


# region User
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
    pwd = fields.CharField(max_length=255, description="密码")
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
# endregion


# region role
class Role(BaseModel):
    """
    角色表

    Args:
        Model (_type_): _description_

    Returns:
        _type_: _description_
    """

    role_name = fields.CharField(max_length=255, description="角色名")
    role_code = fields.CharField(max_length=255, description="角色编码")
    table_description = "角色表"

    def __str__(self):
        return self.name


Role_orm = pydantic_model_creator(Role, name="Role")
Role_in_orm = pydantic_model_creator(Role, name="RoleIn", exclude_readonly=True)
# endregion


# region Organization
class Organization(BaseModel):
    """
    组织机构表

    Args:
        Model (_type_): _description_

    Returns:
        _type_: _description_
    """

    org_level = fields.IntField(description="组织等级")
    org_pid = fields.CharField(max_length=50, description="上级组织id")
    org_code = fields.CharField(max_length=50, description="组织编码")
    org_name = fields.CharField(max_length=50, description="组织名称")
    table_description = "组织机构表"

    def __str__(self):
        return self.name


Organization_orm = pydantic_model_creator(Organization, name="Organization")
Organization_in_orm = pydantic_model_creator(
    Organization,
    name="OrganizationIn",
    exclude_readonly=True,
)
# endregion


# region OrganizationRole
class OrganizationRole(BaseModel):
    """
    组织机构-角色表

    Args:
        Model (_type_): _description_

    Returns:
        _type_: _description_
    """

    # org_id = fields.CharField(max_length=50, description="组织id")
    # role_id = fields.CharField(max_length=50, description="角色id")
    table_description = "组织机构-角色表"
    role = fields.ForeignKeyField(
        "models.Role",
        related_name="role_id",
        db_constraint=False,
    )
    organization = fields.ForeignKeyField(
        "models.Organization",
        related_name="organization_id",
        db_constraint=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        table = "organization_role"


OrganizationRole_orm = pydantic_model_creator(OrganizationRole, name="OrganizationRole")
OrganizationRole_in_orm = pydantic_model_creator(
    OrganizationRole,
    name="OrganizationRole",
    exclude_readonly=True,
)
# endregion
