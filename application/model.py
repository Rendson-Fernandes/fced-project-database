from pydantic import BaseModel


class ConfigDatabase(BaseModel):
    name: str
    user: str
    password: str
    host: str
    port: int

class TeamModel(BaseModel):
    event_year: str 
    event: str
    name: str
    place: int
