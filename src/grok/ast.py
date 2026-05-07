# Abstract Syntax Tree definitions for Grok Language

from dataclasses import dataclass
from typing import List, Any

@dataclass
class ASTNode:
    pass

@dataclass
class Literal(ASTNode):
    value: Any
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

@dataclass
class PrintStatement(ASTNode):
    value: ASTNode
