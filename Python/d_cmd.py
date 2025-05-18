import subs

def D_cmd():
    text=''
    while True:
        if text=='make key':
            enc_key=subs.make_enc_key()
            print('New encrypt key has been created')
        if text=='make de_key':
            dec_key=subs.compute_dec_key(enc_key)
            print('New decrypt key has been created')
        if text=='encrypt':
            encryption=subs.encrypt_text(input('Please enter text to encrypt:'),enc_key)
            print('Encoded text: ',encryption)
        if text=='decrypt':
            decryption=subs.decrypt_text(input('Please enter text to decrypt:'),dec_key)
            print(decryption)
        if text=='exit':
            print('See you again!')
            break
        text=input('enc>')

D_cmd()