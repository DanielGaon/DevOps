import subs

def D_cli():
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
            print('See you next time!')
            break
        text=input('enc>')

#D_cli()


def cli():
    cmds=make_cmds_dict()
    while True:
        cmd=get_user_command(cmds)
        cmds[cmd]()

def get_user_command(cmds):
    while True:
        cmd_candidate=input('encrypt>')
        if cmd_candidate in cmds:
            return cmd_candidate
        else:
            print('Not a valid command-try again')

def handle_mek_cmd():
    pass

def handle_mdk_cmd():
    pass

def handle_enc_cmd():
    pass

def handle_dec_cmd():
    pass

def handle_empty_cmd():
    pass

def make_cmds_dict():
    cmds={}
    cmds['mek'] = handle_mek_cmd
    cmds['mdk'] = handle_mdk_cmd
    cmds['enc'] = handle_enc_cmd
    cmds['dec'] = handle_dec_cmd
    cmds[''] = handle_empty_cmd
    return cmds

cli()