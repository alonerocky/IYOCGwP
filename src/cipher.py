'''
Created on Apr 18, 2014

@author: sli1
'''
MAX_KEY_SIZE = 26

def getMode():
    mode = ''
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input()
        if mode in 'encrypt e decript d'.split( ):
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('Enter your message:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter a key (1-%s)' %(MAX_KEY_SIZE))
        key = int(input())
        if key >= 1 and key <= MAX_KEY_SIZE:
            return key

def encrypt(message,key):
    encrypted = ''
    for ch in message:
        symbol = ch
        if ch.isalpha():
            symbol = chr(ord(symbol) + key)
            if ch.isupper() and symbol > 'Z' or ch.islower() and symbol > 'z':
                symbol = chr(ord(symbol) - 26)
        encrypted += symbol
    return encrypted

def decrypt(message, key):
    decrypted = ''
    for ch in message:
        symbol = ch
        if ch.isalpha():
            symbol = chr(ord(symbol) - key)
            if ch.isupper() and symbol < 'A' or ch.islower() and symbol < 'a':
                symbol = chr(ord(symbol) + 26)
        decrypted += symbol
    return decrypted

def cipher():
    mode = getMode()
    message = getMessage()
    key = getKey()

    if mode[0] == 'e':
        print("your encrpted message is: ")
        print(encrypt(message,key))
    elif mode[0] == 'd':
        print("your decrptyed message is: ")
        print(decrypt(message,key))

cipher()