from pydantic import BaseModel, NameEmail, validator, Field, HttpUrl
from typing import List, Optional

class Get_List_Users_User(BaseModel):
    id: int = Field(ge=1)
    email: NameEmail
    first_name: str = Field(min_length=2, pattern="^[A-Za-zА-Яа-я]*$")
    last_name: str = Field(min_length=2, pattern="^[A-Za-zА-Яа-я]*$")
    avatar: HttpUrl

class Get_List_Users_Support(BaseModel):
    url: HttpUrl
    text: str

class Get_List_Users(BaseModel):
    page: Optional[int] = None
    per_page: Optional[int] = None
    total: Optional[int] = None
    total_pages: Optional[int] = None
    data: List[Get_List_Users_User] = Field(min_length=1)
    support: Get_List_Users_Support

