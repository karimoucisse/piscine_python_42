import string
import sys

def text_analyzer(text=None):
    """This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text."""
    try:
        printable_chr = 0
        upper_chr = 0
        lower_chr = 0
        punctuation_mark_chr = 0
        espace_chr = 0
        while not text:
            text = input("What is the text to analyze?\n")
        assert isinstance(text, str), "argument is not a string"
        for x in text:
            if(x.isprintable()):
                printable_chr = printable_chr + 1
            if(x.isupper()):
                upper_chr = upper_chr + 1
            if(x.islower()):
                lower_chr = lower_chr + 1
            if x in string.punctuation:
                punctuation_mark_chr = punctuation_mark_chr + 1
            if(x == ' '):
                espace_chr = espace_chr + 1
        print(f"The text contains {printable_chr} printable character(s):")
        print(f"- {upper_chr} upper letter(s)")
        print(f"- {lower_chr} lower letter(s)")
        print(f"- {punctuation_mark_chr} punctuation mark(s)")
        print(f"- {espace_chr} space(s)")
    except AssertionError as e:
        print(f"AssertionError: {e}")

def main():
    if(len(sys.argv) != 2):
        print("Error, program should take one arg")
        return
    text_analyzer(sys.argv[1])

if __name__=="__main__":
    main()