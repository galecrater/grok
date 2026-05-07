# Grok REPL

def start_repl():
    print("Grok Language REPL v0.1.0")
    print("The programming language that understands the universe.")
    print("Type 'exit' or Ctrl+C to quit.\n")
    
    while True:
        try:
            line = input("grok> ")
            if line.strip().lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            if line.strip():
                print(f"[Parsed] {line}")
                # TODO: Call parser + interpreter later
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    start_repl()