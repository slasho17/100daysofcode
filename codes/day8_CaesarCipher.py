alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text, shift):
    encryptedText = []
    for character in text:
        characterIndex = alphabet.index(character)
        encryptedText.append(alphabet[characterIndex - shift])
    return encryptedText

def decrypt(text, shift):
    decryptedText = []
    for character in text:
        characterIndex = alphabet.index(character)
        newPos = (characterIndex + shift) % len(alphabet)
        decryptedText.append(alphabet[newPos])
    return decryptedText


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if direction != "decode" and direction != "encode":
    print("Type 'encode' or 'decode'")
    exit()

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    print(''.join(encrypt(text, shift)))
else:
    print(''.join(decrypt(text, shift)))
