from pydantic import BaseModel


class Script(BaseModel):
    def compile(self, prefix: str = "") -> str:
        raise NotImplementedError
