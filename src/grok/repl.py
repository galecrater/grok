from .lexer import Lexer
from .parser import Parser
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
            parser = Parser(tokens)
            ast = parser.parse()
            
            print('→ Parsed successfully')
            interpreter.execute(ast)
            
        except Exception as e:
            print(f'Error: {e}')
