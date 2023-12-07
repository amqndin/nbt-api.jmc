tellraw @a {"nbt": "path.to.array[0]", "interpret": false, "storage": "main"}
data modify storage main path.to.array append from storage main path.to.array[0]
data remove storage main path.to.array[0]
scoreboard players add $i __variable__ 1
execute if score $i __variable__ < $len __variable__ run function jmc:__private__/for_loop/0
