# Parser for Grok Language

from dataclasses import dataclass
from typing import List, Optional
from .lexer import Token
from .ast import *

def parse(tokens: List[Token]) -> List[ASTNode]:
    '''Basic parser stub returning list of AST nodes'''
    if not tokens or tokens[0].type == 'EOF':
        return []
    
    nodes = []
    i = 0
    while i < len(tokens) and tokens[i].type != 'EOF':
        token = tokens[i]
        
        if token.type == 'KEYWORD' and token.value == 'let':
            # Stub: let x = y
            nodes.append(Assignment(
                target=Identifier("placeholder"),
                value=Literal("value", "placeholder")
            ))
            i += 1
        elif token.type == 'KEYWORD' and token.value == 'simulate':
            nodes.append(SimulationBlock(body=[]))
            i += 1
        elif token.type == 'KEYWORD' and token.value == 'observe':
            nodes.append(ObserveStatement(target=Identifier("target")))
            i += 1
        elif token.type == 'KEYWORD' and token.value == 'print':
            nodes.append(PrintStatement(value=Literal("stub", "STRING")))
            i += 1
        else:
            i += 1
    return nodes
