from python.main import *

correct = [
    'data get block ~ ~ ~ Items',
    'data merge entity @s {NoAI:1b,Invulnerable:1b}',
    'data merge entity @s {NoAI:1b,Invulnerable:1b}',
    'data modify storage main some.tag set value 1b',
    'data modify storage main some.tag.array append value 1b',
    'data modify storage main array append from storage temp tempArray[0]',
    'data modify storage main some.path set from entity @s[type=player,tag=!this] SelectedItem.tag.pages',
    'data modify storage main some.string set string block 0 0 0 Items[0] 0 1',
    'data modify storage main some.string append string storage main storage.path 0 1',
    'data remove storage main some.array[0]',
    'data merge block 0 0 0 {Items:[{Slot:0b,id:"minecraft:stone",Count:1b}]}',
    'data modify storage main array[{"somefilter":1b}][0].tag.array[-1][0] set value 1b',
    'data remove block 0 0 0 Items[1]',
    'data modify storage main path.to.array append from storage main path.to.array[0]\r\ndata remove storage main path.to.array[0]',
    'data get entity f81d4fae-7dec-11d0-a765-00a0c91e6bf6 SelectedItem.Count'
]

def test_all():
    global correct
    test_result = []
    test_result += [
        Nbt.get("~ ~ ~ Items"),
        Nbt.merge("@s {NoAI:1b, Invulnerable:1b}"),
        Nbt.merge("@s {NoAI:1b, Invulnerable:1b}"),
        Nbt.modify("main some.tag set 1b"),
        Nbt.modify("main some.tag.array append 1b"),
        Nbt.modify("main array append from temp tempArray[0]"),
        Nbt.modify("main some.path set from @s[type=player, tag=!this] SelectedItem.tag.pages"),
        Nbt.modify('main some.string set string 0 0 0 Items[0] 0 1'),
        Nbt.modify('main some.string append string main storage.path 0 1'),
        Nbt.remove('main some.array[0]'),
        Nbt.merge('0 0 0 {Items:[{Slot:0b,id:"minecraft:stone",Count:1b}]}'),
        Nbt.modify('main array[{"somefilter":1b}][0].tag.array[-1][0] set 1b'),
        Nbt.remove('0 0 0 Items[1]'),
        Nbt.shift_array('main path.to.array'),
        Nbt.get('f81d4fae-7dec-11d0-a765-00a0c91e6bf6 SelectedItem.Count')
    ]
    for test, command in zip(test_result, correct):
        index = test_result.index(test)+1
        if test != command:
            print(f'\n\ntest {index} failed:\n"{test}"\n\ndoesnt match with correct solution\n\n"{command}"')
        else:
            print(f'test {index} passed')

test_all()

