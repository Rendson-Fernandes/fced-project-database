from pydantic import BaseModel


class ConfigDatabase(BaseModel):
    name: str
    user: str
    password: str
    host: str
    port: int
