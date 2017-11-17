#!/Users/bin/python3

# A Dict with Key to Morse Code
key = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        " ": "/",
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
        "," : "--..--",
        ":": "---...",
        "?": "..--..",
        "'": ".----.",
        "-": "-....-",
        "/": "-..-.",
        "(": "-.--.-",
        "@": ".--.-.",
        "=": "-...-",
        "\"": ".-..-.",
}

reverseKey = {b:a for a,b in key.items()}

def encrypt(string):
    #generates a string same as the length of the input
    random = binascii.b2a_hex(os.urandom(len(string)))
    print("The Key is :" +str(random))
    binString=binascii.hexlify(string.encode())
    zipp = zip(binString,random)
    list = ((chr(a^b)) for a,b in zipp)
    jString = (('').join(list))
    encoded = jString.encode()
    encoded = binascii.b2a_hex(encoded)
    return encoded

def doMorse(string):
    encoded=''
    for letter in string:
        if (letter==' '):
            encoded+=' '
        if (letter.upper() in key):
            letter=letter.upper()
            encoded+=(key[str(letter)])+' '
        else:
            error="Invalid Character '"+letter+"' "
            return error
    return encrypt(encoded)
