# Lexer for Grok Language - The programming language that understands the universe

import re
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Token:
    type: str
    value: Optional[str] = None
    line: int = 1
    column: int = 0

    def __repr__(self):
        if self.value is not None:
            return f"Token({self.type}, {repr(self.value)})"
        return f"Token({self.type})"

# Token types
KEYWORDS = {'let', 'if', 'else', 'for', 'while', 'simulate', 'observe', 'probability', 'grok'}

TOKEN_PATTERNS = [
    (r'\s+', None),  # whitespace
    (r'#.*', 'COMMENT'),
    (r'\d+\.\d+', 'FLOAT'),
    (r'\d+', 'INTEGER'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),
    (r'==|!=|<=|>=|->|=>', 'OPERATOR'),
    (r'[=+\-*/<>(){}\[\],.]', 'OPERATOR'),
    (r'"[^"]*"', 'STRING'),
    (r"'[^']*'", 'STRING'),
]

def tokenize(code: str) -> List[Token]:
    '''Tokenize Grok source code'''
    tokens = []
    line_num = 1
    pos = 0
    code_length = len(code)

    while pos < code_length:
        # Handle newlines
        if code[pos] == '\n':
            line_num += 1
            pos += 1
            continue

        matched = False
        for pattern, token_type in TOKEN_PATTERNS:
            regex = re.compile(pattern)
            match = regex.match(code, pos)
            if match:
                value = match.group(0)
                if token_type:  # Not whitespace
                    token_value = value
                    # Check if identifier is actually a keyword
                    if token_type == 'IDENTIFIER' and token_value.lower() in KEYWORDS:
                        token_type = 'KEYWORD'
                    tokens.append(Token(token_type, token_value, line_num, pos))
                pos += len(value)
                matched = True
                break

        if not matched:
            # Unknown character
            tokens.append(Token('UNKNOWN', code[pos], line_num, pos))
            pos += 1

    tokens.append(Token('EOF'))
    return tokens

if __name__ == "__main__":
    test_code = '''
let particle = Electron at 0 m with velocity = 0.9c
simulate {
    observe particle.position
}
'''
    tokens = tokenize(test_code)
    for t in tokens:
        print(t)