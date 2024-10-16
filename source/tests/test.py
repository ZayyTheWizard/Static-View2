"""
    This test code is NOT for production purposes and is only used for testing the AST parser and the pattern matching and vulnerability detection algorithms.
    This test is taking advantage of the vulnerable eval() and input() functions to demonstrate the detection of insecure code patterns.
    The test code is intentionally vulnerable and should not be used as a reference for secure coding practices.
"""


def vulnerable_eval():
    # Vulnerable use of eval() with user input
    user_input = input("Enter a Python expression to evaluate: ")
    result = eval(user_input)  # This directly evaluates user input, which is dangerous
    print(f"Result: {result}")

def vulnerable_input():
    # Insecure use of input() with user data
    user_input = input("Enter something: ")
    print(f"You entered: {user_input}")

if __name__ == "__main__":
    print("Testing vulnerable eval()...")
    vulnerable_eval()

    print("\nTesting vulnerable input()...")
    vulnerable_input()
