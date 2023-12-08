class nbt:
    '''
    split a string into array of words, ignores spaces in any bracket
    '''
    def split_into_words(input_string):
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}',
            '': None
        }
        words, word = [], ''
        inside = ''
        for index, char in enumerate(input_string):
            if char != " ":
                if char in brackets and inside == '':
                    inside = char
                elif inside in brackets and brackets[inside] == char:
                    inside = ''
                word += char
            elif inside == '':
                words.append(word)
                word = ''
        if word:
            words.append(word)
        return words

    '''
    analyze first argumentand determine source type
    '''
    def get_source_type_and_source(words):
        if words[0].startswith("@"):
            source_type = "entity"
        elif words[0][0] in "~^" or words[0].isnumeric() or words[0].isnumeric():
            source_type = "block"
        else:
            source_type = "storage"
        if source_type == "entity":
            source = words.pop(0)
        elif source_type == "block":
            source = " ".join(words[:3])
            del words[:3]
        else:
            source = words.pop(0)
        return source_type, source, words

    def get(syntax):
        words = nbt.split_into_words(syntax)
        source_type, source, words = nbt.get_source_type_and_source(words)
        path = words.pop(0) if words else ""
        return f'data get {source_type} {source} {path}'

    def merge(syntax):
        words = nbt.split_into_words(syntax)
        source_type, source, words = nbt.get_source_type_and_source(words)
        nbt_data = words.pop(0) if words else ""
        return f'data merge {source_type} {source} {nbt_data}'

    def modify(syntax):
        words = nbt.split_into_words(syntax)
        source_type, source, words = nbt.get_source_type_and_source(words)
        path = words.pop(0)

        actions = {
            "set from": {"action": "set from", "del_words": 2},
            "set string": {"action": "set string", "del_words": 2},
            "set": {"action": "set value", "del_words": 1},
            "append from": {"action": "append from", "del_words": 2},
            "append string": {"action": "append string", "del_words": 2},
            "append": {"action": "append value", "del_words": 1},
            "prepend from": {"action": "prepend from", "del_words": 2},
            "prepend string": {"action": "prepend string", "del_words": 2},
            "prepend": {"action": "prepend value", "del_words": 1},
            "insert from": {"action": "insert from", "del_words": 3},
            "insert string": {"action": "insert string", "del_words": 3},
            "insert": {"action": "insert value", "del_words": 2},
            "merge": {"action": "merge value", "del_words": 1},
            "merge from": {"action": "merge from", "del_words": 2},
            "merge string": {"action": "merge string", "del_words": 2}
        }

        action = ""
        start = ""
        end = ""
        index = ""

        for key in actions:
            if key in syntax:
                action = actions[key]["action"]
                del words[:actions[key]["del_words"]]
                if "insert" in key:
                    index = words.pop(0)
                break

        second_source_type = ""
        second_source = ""
        second_path = ""
        if words and action not in ["set value", "append value", "prepend value", "insert value", "merge value"]:
            second_source_type, second_source, words = nbt.get_source_type_and_source(words)
            if words:
                second_path = words.pop(0)

        if action in ["set string", "append string", "prepend string", "insert string", "merge string"] and words:
            start = words.pop(0)
            end = words.pop(0)

        value = ""
        if action in ["set value", "append value", "prepend value", "insert value", "merge value"] and words:
            value = words.pop(0)
            value += " "

        return f'data modify {source_type} {source} {path} {action} {value}{second_source_type} {second_source} {second_path} {index} {start} {end}'.strip()

    def remove(syntax):
        words = nbt.split_into_words(syntax)
        source_type, source, words = nbt.get_source_type_and_source(words)
        path = words.pop(0) if words else ""
        return f'data remove {source_type} {source} {path}'

    def shift_array(syntax):
        words = nbt.split_into_words(syntax)
        source_type, source, words = nbt.get_source_type_and_source(words)
        path = words.pop(0) if words else ""
        return f'data modify {source_type} {source} {path} append from {source_type} {source} {path}[0]\ndata remove {source_type} {source} {path}[0]'
        

