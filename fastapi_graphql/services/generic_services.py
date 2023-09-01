# generic_services.py
from typing import List, Optional, Type, TypeVar, Dict

import strawberry

from fastapi_graphql.model.models import BaseModel, User, User_orm, UserInput, UserType


ModelType = TypeVar("ModelType", bound=BaseModel)
"""
tortoise.models T

Returns:
    _type_: _description_
"""
T = TypeVar("T")
"""
input type

Returns:
    _type_: _description_
"""


class GenericService:
    """
    通用services
    """

    def __init__(self, model_type: Type[ModelType]):
        self.model_type = model_type

    async def create_model(self, data: Dict) -> ModelType:
        """
        新增model

        Args:
            data (Dict): _description_

        Returns:
            ModelType: _description_
        """
        return await self.model_type.create(**data)

    async def update_model(self, data: Dict, pk_id: str) -> ModelType:
        """
        根据id修改

        Args:
            data (Dict): _description_
            pk_id (str): _description_

        Returns:
            ModelType: _description_
        """
        await self.model_type.filter(id=pk_id).update(**data)
        return self.model_type.get(id=pk_id)

    async def del_model(self, pk_id: str) -> int:
        """
        删除model

        Args:
            pk_id (str): _description_

        Returns:
            bool: _description_
        """
        return await self.model_type.filter(id=pk_id).delete()

    async def find_all(self, query_wrapper: Dict) -> List[ModelType]:
        return await self.model_type.all()


class UserService(GenericService):
    def __init__(self):
        super().__init__(User)

    async def save_model(self, model: UserInput) -> Optional[UserType]:
        data_dict = strawberry.asdict(model)
        pk_id = data_dict.pop("id")  # 提取并移除 id 字段
        if pk_id is not None:
            return await User_orm.from_queryset_single(
                await self.update_model(data_dict, pk_id),
            )
        else:
            return await User_orm.from_tortoise_orm(await self.create_model(data_dict))

    async def find_all_user(self, query_wrapper: Dict) -> List[UserType]:
        return await User_orm.from_queryset(await self.find_all)


# Create a dependency to inject UserService instance
def get_user_service() -> UserService:
    return UserService()
