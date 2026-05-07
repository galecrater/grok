from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter

def run_repl():
    print("Grok REPL (v0.1-alpha) — the programming language that understands the universe")
    print("Type 'exit' or Ctrl+D to quit\n")

    interpreter = Interpreter()
    lexer = Lexer()
    parser = Parser()

    while True:
        try:
            line = input("grok> ")
            if line.strip().lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            if not line.strip():
                continue

            tokens = lexer.tokenize(line)
            ast = parser.parse(tokens)
            result = interpreter.interpret(ast)
            if result:
                for r in result:
                    print(f"→ {r}")
        except Exception as e:
            print(f"Error: {e}")
