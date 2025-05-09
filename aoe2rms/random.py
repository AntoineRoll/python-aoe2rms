from pydantic import BaseModel

from aoe2rms import Script
import logging


class RandomChances(Script):
    
    percent_chances: list[tuple[int, Script]]
    
    def model_post_init(self, context):
        total_chances = sum(chance for chance, _ in self.percent_chances)
        if total_chances < 99:
            logging.warning("Total percent chances is below 99. There is a chance that no block is evaluated.")
        if total_chances > 100:
            logging.warning("Total percent chances is above 100. Some blocks may never be evaluated.")
        return super().model_post_init(context)
    
    def compile(self, prefix=""):
        
        result = "start_random\n"
        
        for (percent, script_block) in self.percent_chances:
            compiled_script = script_block.compile(prefix=prefix+"\t")
            result += f"percent_chance {percent}\n{compiled_script}"
            
        result += "end_random\n"
        
        return result
    

class RandomNumber(Script):
    """Generates a script for a random between `min` and `max` included.

    Args:
       min: int
       max: int
    """
    min: int
    max: int
    
    def compile(self, prefix=""):
        return f"{prefix}rnd({self.min},{self.max})\n"