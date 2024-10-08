import ast

def ast_parser(fileLo: str):
    with open(fileLo, 'r') as file:
        astTree = ast.parse(file.read(), mode='exec')

    return astTree
