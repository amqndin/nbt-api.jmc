data get block ~ ~ ~ Items
data merge entity @s {NoAI: 1b, Invulnerable: 1b}
data modify storage main some.tag set value 1b
data modify storage main some.tag.array append value 1b
data modify storage main array append from storage temp tempArray[0]
data modify storage main some.path set from entity @s[type=player, tag=!this] SelectedItem.tag.pages
data modify storage main some.string set string block 0 0 0 Items[0] 0 1
data modify storage main some.string append string storage main storage.path 0 1
data remove storage main some.array[0]
data merge block 0 0 0 {Items: [{Slot: 0b, id: "minecraft:stone", Count: 1b}]}
data modify storage main array[{somefilter: 1b}][0].tag.array[-1][0] set value 1b
data remove block 0 0 0 Items[1]
data modify storage main path.to.array append from storage main path.to.array[0]
data remove storage main path.to.array[0]
