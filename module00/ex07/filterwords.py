from sys import argv
import string


def main():
    if len(argv) != 3:
        return print("ERROR")
    if argv[1].isdigit() or not argv[2].isdigit():
        return print("ERROR")
    wordList = argv[1].split()
    longWordList = list()
    
    for word in wordList:
        new_word = str()
        for i in range(0, len(word)):
            if word[i] not in string.punctuation :
                new_word += word[i]
        # if(not new_word):
        #     new_word = word
        if len(new_word) > int(argv[2]):
            longWordList.append(new_word)
    print(longWordList)

if __name__=="__main__":
    main()