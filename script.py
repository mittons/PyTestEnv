import os

def main():
    test_var = os.getenv('TEST_VAR', 'Not the right value!?')
    s0 = test_var[0]
    s1 = test_var[1:]
    print(f"Env var found: {s0}")
    print(f"Env var found: {s1}")
    
if __name__ == "__main__":
    main()