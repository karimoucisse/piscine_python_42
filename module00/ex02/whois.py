from sys import argv


def odd_even_zero(num):
    if num == 0:
        print("I'm Zero.")
    elif num % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")

def main():
    if(len(argv) < 2):
        return
    try:
        assert len(argv) == 2, "more than one argument is provided"
        assert argv[1].isdigit(), "argument is not an integer"
        num = int(argv[1])
        odd_even_zero(num)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    # except Exception as ex:
    #     print("AssertionError: argument is not an integer")
    

if __name__=="__main__":
    main()
