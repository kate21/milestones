# MilestoneSecretMessage
# DecryptScript

# receiving the cyphered text MilestoneSecretMessage and encryption key
encrypted_text = input("Enter your encrypted text:")
encryption_key = int(input("Enter your key:"))

def decryption(text,key):

    uppercase_plain_sequence = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_plain_sequence = "abcdefghijklmnopqrstuvwxyz"
    decrypted_text = ""

    for encrypted_letter in text:
        if encrypted_letter in uppercase_plain_sequence:
            new_index = (uppercase_plain_sequence.index(encrypted_letter) - key) % len(uppercase_plain_sequence)
            decrypted_text += uppercase_plain_sequence[new_index]
        elif encrypted_letter in lowercase_plain_sequence:  
            new_index = (lowercase_plain_sequence.index(encrypted_letter) - key) % len(lowercase_plain_sequence)
            decrypted_text += lowercase_plain_sequence[new_index]
        else: #for non letters
            decrypted_text += encrypted_letter
    return decrypted_text

encrypted_message = decryption(encrypted_text, encryption_key)
print("Encrypted Message is:" + encrypted_message)