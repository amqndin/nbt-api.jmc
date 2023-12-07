# A better way to interact with nbt in jmc.
generate *any* `/data` command but with a fancy syntax.
```js
Nbt.modify('~ ~ ~ Items set from @s Inventory');
// COMPILES TO:
// data modify block ~ ~ ~ Items set from entity @s Inventory
```
## Syntax
Functions for managing nbt data
- `Nbt.modify(<source> <path> <action> <source|value> [path]);`
- `Nbt.remove(<source> <path>);`
- `Nbt.merge(<source> <raw_nbt>);`
- `Nbt.get(<source> <path>);`

### Clarification
`<source>` - is something that contains nbt data, like coordinates of a block, storage id, or entity selector.

`<path>` - regular nbt path that is used in vanilla `/data` command.

`<raw_nbt>` - raw nbt format like the one that is used in vanilla `/data merge` command

`<action>` - only in `Nbt.modify()`. possible actions are "set", "prepend", "append", "merge", you can add 'from' or 'string' e.g '`append from ...`'.

`<value>` - any valid nbt data, such as object, array, boolean, string, integer, float etc.



### not enough to understand? 
look at `src/beet project/src/data/amandin/jmc/backend/test_cases` in the repo, it should include every syntax.

## Installation
- download the `nbt-api.jmc` file 
- drop the file in your project folder
- import the file with `import "path/to/nbt-api";`

## Enjoy!
