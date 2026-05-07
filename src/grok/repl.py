from .lexer import Lexer
from .parser import parse
from .interpreter import Interpreter

def start_repl():
    print('Grok REPL (v0.2-alpha) — the language that understands the universe')
    print('Type "exit" to quit.\n')
    interpreter = Interpreter()
    
    while True:
        try:
            code = input('grok> ')
            if code.strip().lower() in ['exit', 'quit']:
                print('Goodbye!')
                break
            if not code.strip():
                continue
            
            lexer = Lexer(code)
            tokens = lexer.tokenize()
            ast_nodes = parse(tokens)
            
            print('→ Parsed successfully')
            interpreter.execute(ast_nodes)
            
        except Exception as e:
            print(f'Error: {e}')
