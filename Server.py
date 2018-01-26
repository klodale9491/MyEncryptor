import requests
import urllib.parse as urlparse

import Settings


class Server:

    def __init__(self):
        self.host = "http://myserver/mywebservicepage"
        self.pages = {"userDataManager": "userDataManager.php"}

    def get_page_url(self, page):
        return urlparse.urljoin(Settings.MyEncryptorServerAddress, page)

    def pull_user_data(self, mac):
        page = self.get_page_url(self.pages["userDataManager"])
        get_data = {'mac': mac}
        res = requests.get(url=page, params=get_data)
        # Return user data json (mac, psw) if it's present on the server, otherwise return false
        if res.text != 'NOT_FOUND':
            return {unicode(k).encode("utf-8"): unicode(v).encode("utf-8") for k,v in res.json().iteritems()}
        return False
        
    def push_user_data(self, mac, psw): # If data is already present on server this has no effect
        page = self.get_page_url(self.pages["userDataManager"])
        post_data = {'mac':self.MAC, 'psw':self.Psw}
        res = requests.post(url = page, data = post_data)
        # Return operations success
        res_txt = res.text.encode('ascii','ignore')
        if res_txt == 'OK':
            return True
        return False
