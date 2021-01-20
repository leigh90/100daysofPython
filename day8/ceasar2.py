from art import logo
print(logo)
play = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encrypted_list = [] 
decrypted_list = []  
new_alphabet = alphabet[shift:] + alphabet[:shift]


def ceasarciph(text,shift):
    
    while play:
        if direction == 'encode':
            print(new_alphabet)
            text_indexes = []
            for letter in text:
                for char in alphabet:
                    if letter == char:
                        text_indexes.append(alphabet.index(char))
            print(text_indexes)
            for num in text_indexes:
                encrypted_list.append(new_alphabet[num])
                encrypted_message = ''.join(encrypted_list) 
            print(encrypted_message)

        elif direction == 'decode':
            text_indexes = []
            for letter in text:
                for char in new_alphabet:
                    if letter == char:
                        text_indexes.append(new_alphabet.index(char))
            print(text_indexes)
            for num in text_indexes:
                decrypted_list.append(alphabet[num])
                decrypted_message = ''.join(decrypted_list)
            print(decrypted_message)

ceasarciph(text, shift)
