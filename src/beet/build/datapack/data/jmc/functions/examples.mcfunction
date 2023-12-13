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
data modify entity @s ArmorItems[0].tag set value {display: {color: 16711680}}
data get entity f81d4fae-7dec-11d0-a765-00a0c91e6bf6 SelectedItem.Count
execute store result score $len __variable__ run data get storage main path.to.array
scoreboard players set $i __variable__ 0
execute if score $i __variable__ < $len __variable__ run function jmc:__private__/for_loop/0
