from main import *

class test(nbt):
    def shift_array(syntax):
        words = nbt.split_into_words(syntax)
        source_type, source, words = nbt.get_source_type_and_source(words)
        path = words.pop(0) if words else ""
        return f'''
data modify {source_type} {source} {path} append from {source_type} {source} {path}[0]
data remove {source_type} {source} {path}[0]'''
nbt = test

'''
Nbt.shiftArray('main path.array')
'''

print(nbt.shift_array("@e[type=zombie, limit=1] path.array"))

