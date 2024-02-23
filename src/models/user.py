from pydantic import BaseModel


class User(BaseModel):
    """用户类"""

    name: str
    age: int
