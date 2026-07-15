from sys import argv

def main():
    if(len(argv) < 2) :
        quit()
    strArg = ' '.join(argv[1:]) # join list in str and without element [0]
    reversedStr = strArg[::-1]  # Reverse String 
    swapedStrCase = reversedStr.swapcase() # swap letter case
    print(swapedStrCase)

if __name__=="__main__":
    main()


