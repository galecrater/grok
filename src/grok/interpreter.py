# Grok Interpreter
# Basic execution engine for the Grok language

from .ast import *
from .lexer import TokenType

class Interpreter:
    def __init__(self):
        self.environment = {}
        self.symbols = {}

    def interpret(self, statements):
        results = []
        for stmt in statements:
            result = self.execute(stmt)
            if result is not None:
                results.append(result)
        return results

    def execute(self, node):
        if isinstance(node, LetStatement):
            value = self.evaluate(node.value)
            self.environment[node.name] = value
            return f"{node.name} = {value}"
        elif isinstance(node, PrintStatement):
            value = self.evaluate(node.value)
            print(value)
            return value
        elif isinstance(node, SimulateBlock):
            return "[Simulation started - placeholder for physics engine]"
        else:
            return self.evaluate(node)

    def evaluate(self, node):
        if isinstance(node, NumberLiteral):
            return node.value
        elif isinstance(node, Identifier):
            return self.environment.get(node.name, f"<undefined: {node.name}>")
        elif isinstance(node, BinaryOp):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            if node.op == '+': return left + right
            if node.op == '-': return left - right
            if node.op == '*': return left * right
            if node.op == '/': return left / right
            if node.op == '==': return left == right
        return str(node)
