import re

# Token patterns and corresponding HTML colors
TOKEN_SPECIFICATION = [
    ('KEYWORD', r'\b(if|else|while|for|return|print)\b', 'blue'),
    ('IDENTIFIER', r'[a-zA-Z_]\w*', 'black'),
    ('INTEGER', r'\b\d+\b', 'red'),
    ('OPERATOR', r'[+\-*/=<>]', 'orange'),
    ('STRING', r'\".*?\"', 'green'),
    ('COMMENT', r'#.*', 'gray'),
    ('PARENTHESIS', r'[\(\)]', 'purple')
]

def syntax_highlight(code):
    """
    This function takes source code as input, recognizes tokens, and returns an HTML-formatted string.
    """
    html_code = code
    for token_type, pattern, color in TOKEN_SPECIFICATION:
        html_code = re.sub(pattern, lambda m: f'<span style="color:{color}">{m.group()}</span>', html_code)

    return html_code

def process_file(input_file, output_file):
    """
    Reads code from input_file, applies syntax highlighting, and writes to output_file.
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        code = f.read()

    highlighted_code = syntax_highlight(code)

    # Writing HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"<html><body><pre>{highlighted_code}</pre></body></html>")

# Example usage
process_file('input_code.txt', 'highlighted_output.html')
