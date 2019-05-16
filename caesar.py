#This is a tutorial from the book Invent Your
#Own Computer Games with Python

#Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode(): #defines encryption and decryption
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']: #input encrypt e decrypt or d
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage(): #requests user input
    print('Enter your message: ')
    return input()

def getKey(): #starts the encyption
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key): #defines the translated message after decryptions solved
    if mode[0] == 'd': 
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol
        else:
            #Encrypt or decrypt
            symbolIndex += key
        if symbolIndex >= len(SYMBOLS):
            symbolIndex -= len(SYMBOLS)
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)

        translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode()#call functions
message = getMessage()
key = getKey()
print('Your translated text is: ') #print functions
print(getTranslatedMessage(mode, message, key))