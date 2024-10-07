from tokenizer import CodeTokenizer


if __name__ == "__main__":
    

    file_path = 'source/tests/test.py'
    
    # Initialize tokenizer with the file path
    tokenizer = CodeTokenizer(file_path)
    
    # Tokenize the code
    tokenizer.tokenize_code()

    print(tokenizer.get_tokens())