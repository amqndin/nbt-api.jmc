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

if test_all() == True:
    print('all tests passed succesfully!')
else:
    print(f'\nONE OF THE TESTS FAILED!\n{test_all()}')

