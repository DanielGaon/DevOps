import random
import string

#This function creates encrypted key
def make_enc_key():
    alphabet = string.ascii_lowercase
    shuffled_alphabet = random.sample(alphabet, len(alphabet))
    enc_key=dict(zip(alphabet, shuffled_alphabet))
    return enc_key

#This function creates decrepted key
def compute_dec_key(enc_key):
    dec_key= {v:k for k, v in enc_key.items()}
    return dec_key
        
#This function encrypts the clear text
def encrypt_text(text,enc_key):
    encrypted_text = ''
    for char in text:
        if char in enc_key:
            encrypted_text += enc_key[char]
        else:
            encrypted_text += char
    return encrypted_text

#This function decrypt the encrypted text
def decrypt_text(encrypted_text,dec_key):
    clear_text=''
    for char in encrypted_text:
        if char in dec_key:
            clear_text+=dec_key[char]
        else:
            clear_text+=char
    return clear_text

#Checks all the function
#def full_enc_flow(text):
    enc_key = make_enc_key()
    print(enc_key )
    dec_key = (compute_dec_key(enc_key ))
    print(dec_key)
    enc_text=(encrypt_text(text,enc_key ))
    print(enc_text)
    print(decrypt_text(enc_text,dec_key))

#full_enc_flow(input("Enter phrase to encrypt:"))
