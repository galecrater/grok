# Lexer for Grok Language

class Token:
    def __init__(self, type_: str, value: str = None, line: int = 1, column: int = 0):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"


def tokenize(code: str):
    '''Simple lexer stub - to be expanded'''
    tokens = []
    # Very basic tokenization for now
    for line_num, line in enumerate(code.split('\n'), 1):
        if line.strip():
            tokens.append(Token('LINE', line.strip(), line_num))
    return tokens

# TODO: Full lexer with proper tokens (identifiers, numbers, units, symbols, etc.)