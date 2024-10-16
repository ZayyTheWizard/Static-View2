import ast
from typing import Optional
from tokenizer import CodeTokenizer  # Import CodeTokenizer

def ast_parser(file_lo: str) -> Optional[ast.AST]:
    try:
        # Initialize the CodeTokenizer
        tokenizer = CodeTokenizer(file_lo)
        
        # Tokenize the code (optional: for further debugging)
        tokenizer.tokenize_code()
        print("Tokens from file input:")
        tokenizer.display_tokens()  # Display the tokens if needed
        
        # Proceed with parsing the file into AST
        ast_tree = ast.parse(tokenizer.code, mode='exec')  # Parse the code from tokenizer
        
    except SyntaxError as e:
        print(f"Syntax Error: {e}")
        return None
    except FileNotFoundError as e:
        print(f"File Not Found: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

    return ast_tree

def print_ast_tree(file_lo: str, output_file: str):
    ast_tree = ast_parser(file_lo)
    if ast_tree is not None:
        f = open(output_file, 'w')
        try:
            # ast.dump() returns a formatted string of the AST
            f.write(ast.dump(ast_tree, indent=8))
        finally:
            f.close()
    else:
        f = open(output_file, 'w')
        try:
            f.write("Could not parse the AST.")
        finally:
            f.close()

def extract_functions_from_ast(file_path: str):
    ast_tree = ast_parser(file_lo=file_path)
    functions = []

    for node in ast.walk(ast_tree):
        if isinstance(node, ast.FunctionDef):
            functions.append({
                'name': node.name,
                'lineno': node.lineno,
                'col_offset': node.col_offset,
                'args': [arg.arg for arg in node.args.args]
            })
    
    return functions

if __name__ == "__main__":
    functions = extract_functions_from_ast('source/tests/test.py')
    for func in functions:
        print(f"Function Name: {func['name']}, Line: {func['lineno']}, Args: {func['args']}")