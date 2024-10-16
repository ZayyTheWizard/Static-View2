import ast
from ast_parser import ast_parser


if __name__ == "__main__":
    file_path = 'source/tests/test.py'
    
    astTree = ast_parser(file_path)
    # if astTree is not None:
    #     print(ast.dump(astTree, indent=4))
    # Initialize tokenizer with the file path
    #tokenizer = CodeTokenizer(file_path)
    ## Tokenize the code
    #tokenizer.tokenize_code()
    #ast = syntaxTree(tokenizer.get_tokens())
    #myTree = ast.build_tree()
    #myTree.displayBFS()