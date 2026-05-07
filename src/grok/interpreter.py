import ast
from typing import Any, Dict

class Interpreter:
    def __init__(self):
        self.environment: Dict[str, Any] = {}

    def evaluate(self, node):
        if isinstance(node, dict):  # Simple dict-based AST for now
            if node.get('type') == 'LetStatement':
                value = self.evaluate(node['value'])
                self.environment[node['name']] = value
                return value
            elif node.get('type') == 'PrintStatement':
                value = self.evaluate(node['value'])
                print(value)
                return value
            elif node.get('type') == 'SimulateBlock':
                print("[SIMULATE] Running simulation block...")
                # TODO: Implement proper simulation later
                for stmt in node.get('body', []):
                    self.evaluate(stmt)
                return None
            elif node.get('type') == 'ProbabilityExpression':
                # Simple stub
                return 0.42  # placeholder
        return node  # fallback

    def execute(self, ast_nodes):
        for node in ast_nodes:
            self.evaluate(node)
