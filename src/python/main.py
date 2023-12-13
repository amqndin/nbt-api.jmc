class Nbt: 
    def split_into_words(input_string: str) -> list:
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}',
            '': None
        }
        words, word = [], ''
        inside = ''
        for char in input_string:
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

    def tokenize(syntax) -> dict:
        words = Nbt.split_into_words(syntax)
        index = 0
        tokens = {
            '1': {"type": "", "source": "", "path": ""},
            '2': {"type": "", "source": "", "path": ""},
            'action': '',
            'start': '',
            'end': '',
            'value': ''
        }
        # tokenize first nbt object
        if words[index].startswith("@") or Nbt.is_uuid(words[index]):
            tokens["1"]["type"] = "entity"
            tokens["1"]["source"] = words[index]
        elif any(word[0] in "~^" or word.isnumeric() for word in words[:3]):
            tokens["1"]["type"] = "block"
            tokens["1"]["source"] = " ".join(words[:3])
        else:
            tokens["1"]["type"] = "storage"
            tokens["1"]["source"] = words[index] 
        if tokens["1"]["type"] == "block": index += 3
        else: index += 1
        tokens["1"]["path"] = words[index]
        if words[index] == words[-1]: return tokens

        index += 1 

        # tokenize actions and corresponding value
        if words[index] in ["set", "append", "prepend", "insert", "merge"]:
            if words[index] == 'insert' and words[index+1].isnumeric():
                tokens['action'] = 'insert ' + words[index+1] + " " + words[index+2]
            elif words[index+1] in ['from', 'string']:
                tokens["action"] = " ".join(words[index:index+2])
            else:
                tokens["action"] = words[index] + " value"
                tokens["value"] = words[index+1]
                return tokens
        
        index += 2

        # tokenize second nbt object
        if words[index].startswith("@") or Nbt.is_uuid(words[index]):
            tokens["2"]["type"] = "entity"
            tokens["2"]["source"] = words[index]
        elif any(word[0] in "~^" or word.isnumeric() for word in words[index:index+2]):
            tokens["2"]["type"] = "block"
            tokens["2"]["source"] = " ".join(words[index:index+3])
        else:
            tokens["2"]["type"] = "storage"
            tokens["2"]["source"] = words[index] 
        if tokens["2"]["type"] == "block": index += 3
        else: index += 1
        tokens["2"]["path"] = words[index]
        if words[index] == words[-1]: return tokens
        
        index += 1

        if "string" not in tokens['action']:
            return tokens
        
        # tokenize 'index, start, end'
        tokens['start'] = words[index]
        tokens['end'] = words[index+1]

        return tokens 
    
    def is_uuid(string: str) -> bool:
        parts = string.split('-')
        return len(parts) == 5 and all(len(part) in (8, 4, 4, 4, 12) and part.isalnum() for part in parts)

    def get(syntax: str) -> str:
        tokens = Nbt.tokenize(syntax)
        return f'''data get {tokens['1']['type']} {tokens['1']['source']} {tokens['1']['path']}'''

    def merge(syntax: str) -> str:
        tokens = Nbt.tokenize(syntax)
        return f'''data merge {tokens['1']['type']} {tokens['1']['source']} {tokens['1']['path']}'''

    def remove(syntax: str) -> str:
        tokens = Nbt.tokenize(syntax)
        return f'''data remove {tokens['1']['type']} {tokens['1']['source']} {tokens['1']['path']}'''

    def shift_array(syntax: str) -> str:
        tokens = Nbt.tokenize(syntax)
        return f'''data modify {tokens['1']['type']} {tokens['1']['source']} {tokens['1']['path']} append from {tokens['1']['type']} {tokens['1']['source']} {tokens['1']['path']}[0]\r\ndata remove {tokens['1']['type']} {tokens['1']['source']} {tokens['1']['path']}[0]'''

    def modify(syntax: str) -> str:
        tokens = Nbt.tokenize(syntax)
        return f'''data modify {tokens['1']['type']} {tokens['1']['source']} {tokens['1']['path']} {tokens["action"]} {tokens['value']}{tokens['2']['type']} {tokens['2']['source']} {tokens['2']['path']} {tokens['start']} {tokens['end']}'''.strip()
