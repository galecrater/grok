# Parser for Grok Language

from dataclasses import dataclass
from typing import List, Optional
from .lexer import Token

@dataclass
class ASTNode:
    """Base class for all AST nodes"""
    pass

@dataclass
class Literal(ASTNode):
    value: str
    token_type: str

@dataclass
class Identifier(ASTNode):
    name: str

@dataclass
class Assignment(ASTNode):
    target: Identifier
    value: ASTNode

@dataclass
class SimulationBlock(ASTNode):
    body: List[ASTNode]

@dataclass
class ObserveStatement(ASTNode):
    target: ASTNode

# Simple recursive descent parser stub for Phase 1
def parse(tokens: List[Token]) -> ASTNode:
    '''Basic parser that builds a simple AST'''
    if not tokens or tokens[0].type == 'EOF':
        return None
    
    # Very basic parsing for now - will be expanded
    token = tokens[0]
    
    if token.type == 'KEYWORD' and token.value == 'let':
        return Assignment(
            target=Identifier("placeholder"),
            value=Literal("value", "placeholder")
        )
    
    elif token.type == 'KEYWORD' and token.value == 'simulate':
        return SimulationBlock(body=[])
    
    elif token.type == 'KEYWORD' and token.value == 'observe':
        return ObserveStatement(target=Identifier("target"))
    
    # Default fallback
    return Literal(token.value or "", token.type)

if __name__ == "__main__":
    from .lexer import tokenize
    test_code = "let particle = Electron"
    tokens = tokenize(test_code)
    ast = parse(tokens)
    print(ast)