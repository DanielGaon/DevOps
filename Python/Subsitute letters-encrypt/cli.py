
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