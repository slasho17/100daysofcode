alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text, shift):
    encrypted_text = []
    for character in text:
        character_index = alphabet.index(character)
        encrypted_text.append(alphabet[character_index - shift])
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = []
    for character in text:
        character_index = alphabet.index(character)
        new_pos = (character_index + shift) % len(alphabet)
        decrypted_text.append(alphabet[new_pos])
    return decrypted_text


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
