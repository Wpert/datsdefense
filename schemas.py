from pydantic import BaseModel


class STarget(BaseModel):
    x: int
    y: int

