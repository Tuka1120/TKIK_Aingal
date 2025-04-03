import re

# Define syntax rules for a simple Python highlighter
TOKENS = [
    (r'#[^\n]*', 'comment', 'green'),  # Comments (green)
    (r'\".*?\"|\'.*?\'', 'string', 'brown'),  # Strings (brown)
    (r'\b(if|else|for|while|return|def|class|import|from|as|print|and|or|not|is|in)\b', 'keyword', 'blue'),  # Keywords (blue)
    (r'\b\d+\b', 'number', 'red'),  # Numbers (red)
    (r'[+\-*/=<>!]+', 'operator', 'purple'),  # Operators (purple)
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'identifier', 'black')  # Identifiers (black)
]

def highlight_code(code):
    """Highlight Python code with HTML formatting."""
    def replacer(match):
        for pattern, token_type, color in TOKENS:
            if re.fullmatch(pattern, match.group(0)):
                return f'<span style="color:{color}">{match.group(0)}</span>'
        return match.group(0)  # Default case

    # Combine all regex patterns
    combined_pattern = '|'.join(f'({pattern})' for pattern, _, _ in TOKENS)
    
    # Apply regex substitution with color formatting
    highlighted_code = re.sub(combined_pattern, replacer, code)

    # Wrap in HTML
    return f'<html><body><pre>{highlighted_code}</pre></body></html>'

def read_code_from_file(filename):
    """Read code from a text file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

# Read code from input_code.txt
code_snippet = read_code_from_file("input_code.txt")

if code_snippet:
    # Highlight the code
    html_output = highlight_code(code_snippet)
    
    # Save to an HTML file for preview
    with open("highlighted_output.html", "w", encoding="utf-8") as file:
        file.write(html_output)
    
    print("Syntax highlighting complete! Check highlighted_code.html")
