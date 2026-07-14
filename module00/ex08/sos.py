from sys import argv 
# from MorseCodePy import encode


MORSEDICT = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}

def isMorseCharacter(text):
    morse_code = "./-"
    for c in text:
        if morse_code.find(c) != -1:
            return True
    return False

def printMorseCharacter(c):
    if c == ' ':
        return '/'
    else:
        return MORSEDICT[c.lower()]

def main():
    if len(argv) < 2:
        quit()
    text_list = argv[1:]
    for text in text_list:
        if isMorseCharacter(text):
            return print("ERROR")
    morse_text = str()
    for x in range(0, len(text_list)):
        for c in range(0, len(text_list[x])):
            morse_text += printMorseCharacter(text_list[x][c])
            if(x < len(text_list[x]) - 1):
                morse_text += ' '
        if(x < len(text_list) - 1):
            morse_text += '/ '
    print(morse_text)


if __name__=="__main__":
    main()