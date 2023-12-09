# assume that only lower case letters need to be encrypted
letters = 'abcdefghijklmnopqrstuvwxyz'


def caesar_cipher(plaintext, key):
    cipherlist = []
    letters_len = len(letters)
    for c in plaintext:
        pos = letters.index(c)
        pos = (pos + key) % letters_len
        cipherlist.append(letters[pos])
    return ''.join(cipherlist)


plaintext = input('Enter the plaintext: ')
key = input('Enter the key: ')
key = int(key)
ciphertext = caesar_cipher(plaintext, key)
print(ciphertext)

# Explorer task
def caesar_decrypt(ciphertext, key):
    return caesar_cipher(ciphertext, -key)

print('decrypt: ', caesar_decrypt(ciphertext, key))
