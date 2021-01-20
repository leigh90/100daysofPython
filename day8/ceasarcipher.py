alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encrypted_list = [] 
decrypted_list = []  
new_alphabet = alphabet[shift:] + alphabet[:shift]
# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.te

def encrypt(text,shift):
    # rotate list
    new_alphabet = alphabet[shift:] + alphabet[:shift]
    print(new_alphabet)
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    # encrypt message
    
    # find the original indexes of the message
    text_indexes = []
    for letter in text:
        for char in alphabet:
            if letter == char:
                text_indexes.append(alphabet.index(char))
    print(text_indexes)

    # get new indexes
    for num in text_indexes:
        encrypted_list.append(new_alphabet[num])
        encrypted_message = ''.join(encrypted_list)
    print(encrypted_message)
      



#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# encrypt(text,shift)


def decrypt(text, shift):
    # get indexes of new alphabet
    text_indexes = []
    for letter in text:
        for char in new_alphabet:
            if letter == char:
                text_indexes.append(new_alphabet.index(char))
    print(text_indexes)
    # match to old alphabet

    for num in text_indexes:
        decrypted_list.append(alphabet[num])
        decrypted_message = ''.join(decrypted_list)
    print(decrypted_message)


# decrypt(text,shift)

if direction == 'encode':
    encrypt(text,shift)
elif direction == 'decode':
    decrypt(text,shift)




#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_text, shift_amount):
#   #TODO-2: Inside the encrypt function, shift each letter of the text forwards in the alphabet by the shift amount and print the encrypted text.  
#   #e.g. 
#   #plain_text = "hello"
#   #shift = 5
#   #cipher_text = "mjqqt"
#   #print output: "The encoded text is mjqqt"
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# encrypt(plain_text=text, shift_amount=shift)
# def decrypt(plain_text, shift_amount):
#   #TODO-2: Inside the encrypt function, shift each letter of the text forwards in the alphabet by the shift amount and print the encrypted text.  
#   #e.g. 
#   #plain_text = "hello"
#   #shift = 5
#   #cipher_text = "mjqqt"
#   #print output: "The encoded text is mjqqt"
    # cipher_text = ""
    # for letter in plain_text:
    #     position = alphabet.index(letter)
    #     new_position = position - shift_amount
    #     new_letter = alphabet[new_position]
    #     cipher_text += new_letter
    # print(f"The encoded text is {cipher_text}")