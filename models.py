# models.py

from typing import Optional
from pydantic import BaseModel


class Employee(BaseModel):
    id: int
    name: str
    experience: int


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    experience: Optional[int] = None