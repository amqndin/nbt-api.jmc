def nbt(syntax):
    words, word, inside = [], '', ''
    for c in syntax:
        if not inside:
            if c == ' ':
                if word: words.append(word); word = ''
            elif c in ['[', '{', '(', '\'', '"']:
                if word: words.append(word)
                word, inside = c, c
            else: word += c
        else:
            if (c == ']' and inside == '[') or (c == '}' and inside == '{') or (c == ')' and inside == '(') or (c == inside and inside in ['\'', '"']):
                word += c; words.append(word); word, inside = '', ''
            else: word += c
    if word: words.append(word)

    # Initialize variables
    source_type = ""
    source = ""
    operation = ""
    action = ""
    second_source_type = ""
    second_source = ""
    second_path = ""

    # Determine the source type and source
    if words[0].startswith("@"):
        source_type = "entity"
        source = words.pop(0)
    elif any(x in words[0] for x in ["~", "^"]) or words[0].isnumeric():
        source_type = "block"
        source = " ".join(words[:3])
        del words[:3]
    else:
        source_type = "storage"
        source = words.pop(0)

    # Determine the path
    path = words.pop(0)

    # Determine the operation and action
    if "set from" in syntax:
        operation = "modify"
        action = "set from"
        del words[:2]
    elif "set" in syntax:
        operation = "modify"
        action = "set value"
        words.pop(0)
    elif "merge" in syntax:
        operation = "merge"
        words.pop(0)
    elif "remove" in syntax:
        operation = 'remove'
        words.pop(0)
    else:
        operation = "get"

    # Determine the second source type and second source
    if words and action != "set value":
        if words[0].startswith("@"):
            second_source_type = "entity"
            second_source = words.pop(0)
        elif any(x in words[0] for x in ["~", "^"]) or words[0].isnumeric():
            second_source_type = "block"
            second_source = " ".join(words[:3])
            del words[:3]
        else:
            second_source_type = "storage"
            second_source = words.pop(0)

    # Determine the second path
    if words and action != "set value":
        second_path = words.pop(0)

    # Determine the value for 'set value' action
    value = ""
    if action == "set value" and words:
        value = words.pop(0)
        value += " "

    # Print the result
    print(f'data {operation} {source_type} {source} {path} {action} {value}{second_source_type} {second_source} {second_path}')

nbt("0 ^ ~ Items")
nbt("@s {NoAI:1b, Invulnerable:1b} merge")
nbt("main some.path set from @s SelectedItem.tag.pages")
nbt("main some.tag set 1b")