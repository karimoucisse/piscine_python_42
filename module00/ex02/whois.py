import sys


def odd_even_zero(num):
    if num == 0:
        print("I'm Zero.")
    elif num % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")

def main():
    if(len(sys.argv) < 2):
        return
    try:
        assert len(sys.argv) == 2, "more than one argument is provided"
        num = int(sys.argv[1])
        odd_even_zero(num)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as ex:
        print("AssertionError: argument is not an integer")
    

if __name__=="__main__":
    main()
