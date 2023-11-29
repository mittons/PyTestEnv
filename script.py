import os

def main():
    test_var = os.getenv('TEST_VAR', 'Not the right value')
    print(f"Env var found: {test_var}")
    
if __name__ == "__main__":
    main()