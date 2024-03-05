# arvhived 3/5/2024
no longer needed since a51e32a commit in official jmc repo (WingedSeal/jmc)

# A better way to interact with nbt in jmc.

generate _any_ `data` command with a fancy syntax.

you can [skip to installation](#install) too.

### Usage example

```js
// replace `data` commands with fancy syntax
Nbt.modify('main some.path set from @s SelectedItem.Count');
Nbt.modify('@s teleport_duration set 1');
Nbt.remove('~ ~1 ~ Items[0]');
Nbt.merge('@s {Invulnerable:1b, Silent:1b, NoGravity:1b}');

// assign variables to NBT values
$array_len = Nbt.get('main path.to.array');

// iterate through arrays
for ($i = 0; $i < $array_len; $i++) {
    tellraw @a {"storage":"main","nbt":"path.to.array[0]"};
    Nbt.shiftArray('main path.to.array');
}
```

## Syntax

Functions for managing nbt data

-   `Nbt.modify(<source> <path> <action> <source|value> [path]);`
-   `Nbt.remove(<source> <path>);`
-   `Nbt.merge(<source> <raw_nbt>);`
-   `Nbt.get(<source> <path>);`
-   `Nbt.shiftArray(<source> <path.to.array>);`

### Clarification

`<source>` is something that contains nbt data, like coordinates of a block, storage id, or entity selector.

`<path>` regular nbt path that is used in vanilla `/data` command.

`<path.to.array>` nbt path that leads to an array and has no index specification

`<raw_nbt>` raw nbt format like the one that is used in vanilla `/data merge` command

`<action>` only in `Nbt.modify()`. possible actions are "set", "prepend", "append", "merge", you can add 'from' or 'string' e.g '`append from ...`'.

`<value>` - any valid nbt data, such as object, array, boolean, string, integer, float etc.

might also wanna check this out `src/beet project/src/data/amandin/jmc/backend/examples` in the repo, it should include every syntax.

## Install

-   download the `nbt-api.jmc` file
-   drop the file in your project folder
-   import the file with `import "path/to/nbt-api";`

## Enjoy!
