import requests
import urllib.parse as urlparse

class Server:

    host = "http://myserver/mywebservicepage"
    pages = {"userDataManager" : "userDataManager.php"}
    
    def getPageUrl(self, page):
        return urlparse.urljoin(Settings.MyEncryptorServerAddress, page)

    def pullUserData(self, mac):

        page = self.getPageUrl(self.pages["userDataManager"])
        get_data = {'mac': mac}
        
        res = requests.get(url=page, params=get_data)

        # Return user data json (mac, psw) if it's present on the server, otherwise return false
        if res.text != 'NOT_FOUND':
            return {unicode(k).encode("utf-8"): unicode(v).encode("utf-8") for k,v in res.json().iteritems()}
        
        return False
        
    def pushUserData(self, mac, psw): # If data is already present on server this has no effect

        page = self.getPageUrl(self.pages["userDataManager"])
        post_data = {'mac':self.MAC, 'psw':self.Psw}

        res = requests.post(url = page, data = post_data)
        
        # Return operations success
        res_txt = res.text.encode('ascii','ignore')
        if res_txt == 'OK':
            return True
        return False