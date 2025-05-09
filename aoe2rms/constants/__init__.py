from aoe2rms import Script


class Constant(Script):
    id: int
    name: str
    description: str | None = None
    _type: str
    _valid_id_list = list

    def model_post_init(self, context):

        if self.id not in self._valid_id_list:
            raise ValueError(f"Provided id {self.id} is not a valid {self._type} ID.")
        
        if self.description:
            self.__doc__ = self.description

        return super().model_post_init(context)

    def declare(self):
        declare_str = f"#const {self.name} {self.id}"
        if desc := self.description:
            declare_str += f" /* {desc} */"
        declare_str += "\n"
        return declare_str
    
    def compile(self, prefix=""):
        return prefix + self.name

    def __str__(self):
        return self.name


class TerrainConstant(Constant):
    _type = "terrain"
    _valid_id_list = range(200)
