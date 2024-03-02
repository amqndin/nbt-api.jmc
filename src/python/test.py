from main import *

def test():
    pass

print(test())

# print(Nbt.get('0 0 0 Items[0]tag.'))
test_case = "main some.string append string main storage.path 0 1"
# test_case = "0 0 0 Items[0] set from 0 0 0 SelectedItem"

print(f'{Nbt.tokenize(test_case)}')
print("")
print(f"{Nbt.modify(test_case)}')")


