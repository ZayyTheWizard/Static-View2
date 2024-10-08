import ast
from typing import Optional

def ast_parser(fileLo: str) -> Optional[ast.AST]:
    try:
        with open(fileLo, 'r') as file:
            astTree = ast.parse(file.read(), mode='exec')
    except SyntaxError as e:
        print(f"Syntax Error: {e}")
        return None
    except FileNotFoundError as e:
        print(f"File Not Found: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

    return astTree
