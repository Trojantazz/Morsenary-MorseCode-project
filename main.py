logo = """

                                                                                                                   
          ____      ,----..                                             ,--.                                       
        ,'  , `.   /   /   \  ,-.----.     .--.--.       ,---,.       ,--.'|   ,---,       ,-.----.                
     ,-+-,.' _ |  /   .     : \    /  \   /  /    '.   ,'  .' |   ,--,:  : |  '  .' \      \    /  \         ,---, 
  ,-+-. ;   , || .   /   ;.  \;   :    \ |  :  /`. / ,---.'   |,`--.'`|  ' : /  ;    '.    ;   :    \       /_ ./| 
 ,--.'|'   |  ;|.   ;   /  ` ;|   | .\ : ;  |  |--`  |   |   .'|   :  :  | |:  :       \   |   | .\ : ,---, |  ' : 
|   |  ,', |  ':;   |  ; \ ; |.   : |: | |  :  ;_    :   :  |-,:   |   \ | ::  |   /\   \  .   : |: |/___/ \.  : | 
|   | /  | |  |||   :  | ; | '|   |  \ :  \  \    `. :   |  ;/||   : '  '; ||  :  ' ;.   : |   |  \ : .  \  \ ,' ' 
'   | :  | :  |,.   |  ' ' ' :|   : .  /   `----.   \|   :   .''   ' ;.    ;|  |  ;/  \   \|   : .  /  \  ;  `  ,' 
;   . |  ; |--' '   ;  \; /  |;   | |  \   __ \  \  ||   |  |-,|   | | \   |'  :  | \  \ ,';   | |  \   \  \    '  
|   : |  | ,     \   \  ',  / |   | ;\  \ /  /`--'  /'   :  ;/|'   : |  ; .'|  |  '  '--'  |   | ;\  \   '  \   |  
|   : '  |/       ;   :    /  :   ' | \.''--'.     / |   |    \|   | '`--'  |  :  :        :   ' | \.'    \  ;  ;  
;   | |`-'         \   \ .'   :   : :-'    `--'---'  |   :   .''   : |      |  | ,'        :   : :-'       :  \  \ 
|   ;/              `---`     |   |.'                |   | ,'  ;   |.'      `--''          |   |.'          \  ' ; 
'---'                         `---'                  `----'    '---'                       `---'             `--`  
                                                                                                                   

"""

print(logo)
print("Welcome to Morsenary your trusted Morse Code cypher tool!")

""" A dictionary of standard morse language with letters as keys and morse code as values."""
morse = {
    # Letters
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
    # Numbers
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
    # Punctuation
    "&": ".-...",
    "'": ".----.",
    "@": ".--.-.",
    ")": "-.--.-",
    "(": "-.--.",
    ":": "---...",
    ",": "--..--",
    "=": "-...-",
    "!": "-.-.--",
    ".": ".-.-.-",
    "-": "-....-",
    "+": ".-.-.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
}


def cypher():
    """ A function that allows user to select cypher method(user can translate morse code to plain text or plain
         text to morse code. """
    cypher_method = input("To encrypt text type e and to decrypt morse code type d! ").lower()
    if cypher_method == "e":
        text = input("Type the text here. ")
        encrypt_text(plain_text=text)

    elif cypher_method == "d":
        text = input("Type the text here. ")
        decrypt_text(morse_code=text)

    else:
        print("Sorry you have entered a wrong method,try again!")
        return cypher()


def decrypt_text(morse_code, strict=True):
    """
    Translates morse code to english.
    Accepts:
        morse (str): A string of morse code to translate
        strict (bool): If True, parse and return morse code containing 4 spaces
    Returns:
        str: A translated string of text
    """

    if morse_code == "":
        print("You must provide a string of text to translate")

    if "    " in morse_code:
        if strict:
            print("Unable to translate morse code. Found 4 spaces in morse code string")
        else:
            morse_code.replace("    ", "   ")

    translation = ""

    words = morse_code.split("   ")

    for morse_word in words:
        chars = morse_word.split(" ")
        for char in chars:
            for k, v in morse.items():
                if char == v:
                    translation += k
        translation += " "

    print(translation.rstrip())


def encrypt_text(plain_text):
    """
    Translates text to morse code.
    Accepts:
        text (str): A string of text to translate
    Returns:
        str: A translated string of morse code
    """

    if plain_text == "":
        print("You must provide a morse code string to translate")

    translation = ""
    words = plain_text.split(" ")
    for word in words:
        w = list()
        for char in word:
            if char.lower() in morse:
                w.append(morse[char.lower()])
        translation += " ".join(w)
        translation += "   "
    print(translation.rstrip())


cypher()
