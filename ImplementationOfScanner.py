import re

# Define token patterns
TOKEN_SPECIFICATION = [
    ('INTEGER', r'\d+'),          # Integer numbers
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),  # Variable names
    ('ADD', r'\+'),               # Addition
    ('SUBTRACT', r'-'),           # Subtraction
    ('MULTIPLY', r'\*'),          # Multiplication
    ('DIVIDE', r'/'),             # Division
    ('LPAREN', r'\('),            # Left parenthesis
    ('RPAREN', r'\)'),            # Right parenthesis
    ('WHITESPACE', r'\s+'),       # Whitespace (ignored)
    ('UNKNOWN', r'.')             # Any other character (error)
]

# Compile regex patterns
token_re = re.compile('|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in TOKEN_SPECIFICATION))

def scanner(code):
    tokens = []
    for match in token_re.finditer(code):
        token_type = match.lastgroup
        token_value = match.group(token_type)

        if token_type == 'WHITESPACE':  # Skip whitespace
            continue
        elif token_type == 'UNKNOWN':  # Handle errors
            print(f"Lexical error: Unexpected character '{token_value}' at position {match.start()}")
        else:
            tokens.append((token_type, token_value))

    return tokens

# Example expression
expression = "2 + 3 * (76 + 8 / 3) + 3 * (9 - 3)"
tokens = scanner(expression)

# Print tokens
for token in tokens:
    print(token)
