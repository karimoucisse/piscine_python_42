from sys import argv

def alignLength(text):
    return max(len(text) + 2)
def calculus(a, b):
    print(f"Sum: {a + b:>9}")
    print(f"Difference: {a - b:>2}")
    print(f"Product: {(a * b):>6}")
    if a == 0 or b == 0:
        print("Quotient: ERROR (division by zero)\nRemainder: ERROR (modulo by zero)")
    else:
        print(f"Quotient: {a / b:>5}")
        print(f"Remainder: {a % b:>2}")

def main():
    try:
        if(len(argv) < 2):
            return print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
        assert len(argv) == 3, "too many arguments"
        for i in argv[1:] :
            assert i.isnumeric(), "only integers"
        calculus(int(argv[1]), int(argv[2]))
    except AssertionError as e:
        print(f"AssertionError: {e}")
    
if __name__=="__main__":
    main()