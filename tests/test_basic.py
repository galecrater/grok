# Basic tests for Grok Language

def test_lexer():
    from src.grok.lexer import tokenize
    tokens = tokenize("let x = 42 m/s")
    assert len(tokens) > 0
    print("Lexer test passed")

if __name__ == "__main__":
    test_lexer()
    print("All basic tests passed!")