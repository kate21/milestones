# MilestoneSecretMessage
# EncryptionScript

# receiving the plain text MilestoneSecretMessage and encryption key
plain_text = input("Enter your text:")
encryption_key = int(input("Enter your key:"))

#when 26 is entered the cypher loops to the original text
while True:
    if encryption_key == 26: 
        print("The cipher does not work with this key")
        encryption_key = int(input("Enter another key:"))
    else:
        break

def encryption(text,key):

    uppercase_plain_sequence = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_plain_sequence = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""

    for plain_letter in text:
        if plain_letter in uppercase_plain_sequence:
            new_index = (uppercase_plain_sequence.index(plain_letter) + key) % len(uppercase_plain_sequence)
            encrypted_text += uppercase_plain_sequence[new_index]
        elif plain_letter in lowercase_plain_sequence:  
            new_index = (lowercase_plain_sequence.index(plain_letter) + key) % len(lowercase_plain_sequence)
            encrypted_text += lowercase_plain_sequence[new_index]
        else: #for non letters
            encrypted_text += plain_letter
    return encrypted_text

encrypted_message = encryption(plain_text, encryption_key)
print("Encrypted Message is:" + encrypted_message)