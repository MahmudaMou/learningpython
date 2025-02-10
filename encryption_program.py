import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)
#print(chars)
#print(key)
massage = input("Enter the massage that need to be encrypted: ")
cipher_text = ""
plain_text = ""

#Encryption
for x in massage:
    index = chars.index(x)
    cipher_text += key[index]
#Decryption
for x in cipher_text:
    index = key.index(x)
    plain_text += chars[index]

print(f"Your massage is : {massage}")
print(f"Encrypted massage is: {cipher_text}")
print(f"Decrypted massage is: {plain_text}")