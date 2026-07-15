from sys import argv

TAB = 11


def calculus(a, b):
    print(f"{"Sum:".ljust(TAB)} {a + b}")
    print(f"{"Difference:".ljust(TAB)} {a - b}")
    print(f"{"Product:".ljust(TAB)} {(a * b)}")
    if a == 0 or b == 0:
        print(f"{"Quotient:".ljust(TAB)} ERROR (division by zero)\n{"Remainder:".ljust(TAB)} ERROR (modulo by zero)")
    else:
        print(f"{"Quotient:".ljust(TAB)} {a / b}")
        print(f"{"Remainder:".ljust(TAB)} {a % b}")

def main():
    try:
        if(len(argv) < 2):
            print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
            quit()
        assert len(argv) == 3, "too many arguments"
        for i in argv[1:] :
            assert i.isnumeric(), "only integers"
        calculus(int(argv[1]), int(argv[2]))
    except AssertionError as e:
        print(f"AssertionError: {e}")
    
if __name__=="__main__":
    main()