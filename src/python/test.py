from mecha import Mecha
from main import *

mc = Mecha()

def test():
    output = ""
    testing = [
        nbt_modify("foo:bar foo[0].bar set from ERROR_HERE @s Health"),
        nbt_get("foo:bar foo[0].bar")
    ]
    
    for i in testing:
        output += i + "\n"
        
    return output

parsed = mc.parse(test())

try:
    print(mc.serialize(parsed))
except ExceptionGroup as err:
    print(err)
