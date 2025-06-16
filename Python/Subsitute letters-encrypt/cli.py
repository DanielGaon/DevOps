import subs
def cli():
    cmds=make_cmds_dict()
    while True:
        cmd=get_user_command(cmds)

def get_user_command(cmds):
    while True:
        cmd_candidate=input('encrypt>')
        if cmd_candidate in cmds:
            return cmd_candidate
        else:
            print('Not a valid command-try again')

def handle_mek_cmd():
    mek=subs.make_enc_key()
    return mek

def handle_mdk_cmd():
    mdk=subs.compute_dec_key(handle_mek_cmd())
    return mdk

def handle_enc_cmd():
    enc=subs.encrypt_text(get_user_command(),handle_mek_cmd())
    return enc

def handle_dec_cmd():
    dec=subs.decrypt_text()
    return dec

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