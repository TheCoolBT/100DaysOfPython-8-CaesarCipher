# Alphabet is written twice to prevent "index out of bounds" error in the caesar function
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]


# Takes in plaintext message, the shift number, and if it is being encoded or decoded and preformes the caesar cipher
def caesar(plaintext, shift, direction):
    ciphertext = ''
    # If the message is being decoded it will be shifted in the opposite direction than it is being encoded
    if direction == 'decode':
        shift *= -1

    for letter in plaintext:
        # Cipher only works on letter in the alphabet so numbers and characters are left unchanged
        if letter in alphabet:
            position = alphabet.index(letter.lower())
            new_position = position + shift
            new_letter = alphabet[new_position]
            ciphertext += new_letter
        else:
            ciphertext += letter

    print(f"{direction}d text is: {ciphertext}")


print('Welecome to Caesar Cipher')
# Used while loop to force user to type in only things that program can handle
while True:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt").lower()
    if direction != 'encode' and 'decode':
        # User must type in encode or decode otherwise the program loops
        print("Please type 'encode' or 'decode'")
    else:
        plaintext = input("Type the message you want to encrypt or decrypt").lower()
        shift = input("Type the shift number of the cipher")
        if shift.isdigit():
            shift = int(shift)
            # Used modulo so if user types in number greater than 26 for the shift, it will still work as intended
            shift = shift % 26
            caesar(plaintext, shift, direction)
            # Breaks the while loop and ends program if user types in 'n'
            goagain = input("Would you like to go again? (y/n)")
            if goagain.startswith('n'):
                break
        else:
            # User must type in an integer otherwise the program loops
            print("Please type an integer")
