import random 
import string
import time
from colorama import Fore,init
all_char=string.ascii_letters + string.digits +string.punctuation
jion="".join(random.choice(all_char) for i in range(8))
init()
class passwords:
        
      
       def __init__(self,passwordenter,username):
           
           self.username=username
           self.passwordenter=passwordenter
       def appendpassword(self):
           try:
             with open("password","r")as f:
                s=f.read()
           except FileNotFoundError :
              s=" "
           
           
           if self.passwordenter in s or self.username in s:
                   print(Fore.RED + "Password already exists! ⚠️")
           else:
               
               
               with open("password","a+") as f:
                       print(Fore.MAGENTA + " you successfully save  password 🥰🥰🥰")
                       p=f.write(f"username={self.username}\npassword={self.passwordenter}\n {" "}\n")
       def __str__(self):
           return(Fore.YELLOW +"than you !!!👌👌👌👌👌")
  
while True:
   try:

     
        
     
     while True:
         
         username=input(Fore.MAGENTA + "enter the username:::").upper()
         print(Fore.LIGHTMAGENTA_EX +    f"password suggestion ::: {jion}")
         time.sleep(2)
    
         suggestion=input(Fore.GREEN + " you write the password  suggestion in your password :🧐🧐🧐🧐::type :yes::::::").lower()
         
         if suggestion =="yes":
            passwordenter=jion
            p= passwords(passwordenter,username)
            p.appendpassword()
                                 
            print(p)
                 
         else:
             passwordenter=input(Fore.BLUE + "enter the password::")
             
             print("its ok !!!😊😊😊😊")
             p= passwords(passwordenter,username)
             p.appendpassword()
                     
             print(p)
     
   except Exception as e:
       print(e)

     
    