# A better way to interact with nbt in jmc.
## Usage
```js
Nbt.remove("amandin:main array[0]");
// data remove storage amandin:main array[0]

Nbt.get('0 0 0 Items[0]');
// data get block 0 0 0 Items[0]

Nbt.merge('@s {NoGravity:1b, Invulnerable:1b}');
// data merge entity @s {NoGravity:1b, Invulnerable:1b}

Nbt.modify('0 0 0 Items set from @s Inventory');
// data modify block 0 0 0 Items set from entity @s Inventory
```
it should make sense to you after looking at these examples, if it doesnt you can always look at the source code. It can pretty much generate any `/data` command possible even the `/data modify ... string` command.

## Installation
- download the `nbt-api.jmc` file 
- drop the file in your project folder
- import the file with `import "path/to/the/file";`

### good luck, and enjoy.
