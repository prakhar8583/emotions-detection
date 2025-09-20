from pydantic import BaseModel

class APIOutput(BaseModel):
    emotion: str
    time_elapse:str
    time_elapse_for_loading :str