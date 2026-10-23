import webbrowser
from datetime import datetime,date
import time

from colorama  import Fore,init
init()
sites = {
    "github": "https://github.com",
    "facebook": "https://facebook.com",
    "instagram": "https://instagram.com",
    "linkedin": "https://linkedin.com",
    "twitter": "https://x.com",
    "amazon": "https://amazon.in",
    "flipkart": "https://flipkart.com",
    "wikipedia": "https://wikipedia.org",
    "stackoverflow": "https://stackoverflow.com",
    "reddit": "https://reddit.com",
    "claude": "https://claude.com",
    "youtube":"https://youtube.com",
    "google":"https://google.com ",
    "chatgpt":"https://www.chatgpt.com"
}
class website:
    def __init__(self,namesite):
       self.namesite=namesite
    
    def launcher(self):
        webbrowser.open(sites[self.namesite])
        t=datetime.now().strftime("%H:%M:%S")
        d=date.today()
        with open("text.www","w") as f:
            
            s=f.write(str(f"last search::{self.namesite} \n time::{ t} \n date::{str(d)}"))
            print(s)
    @staticmethod
    def print():
        return Fore.GREEN + "thank you"
while True:
    # try:
       
       namesite=input(Fore.GREEN + "search the website:::::").lower()
    
       for site in sites.keys():
        if namesite==site:
          print("successfully open 🤓🤓🤓🤓🤓")
          w=website(namesite)
          w.launcher()
          w.print()
       
           
       if namesite==" ":
          break
    # except Exception as e:
        # print(Fore.RED + "error!!!!!!!☠️",e)
        # print(Fore.BLUE + "try agin 🧐🧐🧐🧐",e)