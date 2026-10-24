morse_alphabet = \
{
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

    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",

    " ": "/",
}



def convert(string):
    morse = ""
    try:
        for char in string.lower():
            morse += morse_alphabet[char]+" "
    except KeyError:
        return "String contains unsupported characters"
    
    return morse



def translate(morse):
    morse_chars = []

    while not morse in morse_alphabet.values():

        morse_char = morse[:morse.find(" ")]

        if not morse_char in morse_alphabet.values():
            return "Invalid morse sequence"

        morse_chars.append(morse_char)

        i = morse.find(" ")+1
        morse = morse[i:]

    morse_chars.append(morse)

    string = ""
    for morse_char in morse_chars:
        for key, value in morse_alphabet.items():
            if morse_char == value:
                string += key

    return string