#Attendance Project
import time 
import datetime

from colorama import Fore,init
init()


d={1:"prince kumar yadav",2:"priya rani birua",3:"raj sharma",4:"ranita hembram",5:"reyan sawaiyan",
   6:"md shabib akram",7:"shagufta perween",8:"unzele fatima",9:"vaibhavi gupta",10:"siddharth kumar upadhyay"}

class attends:
    def __init__(self,n,totale,student):
        self.totale=totale
        self.n=n
        self.student=student
    
    
    
    def check(self ):

    
      for self.stud in self.student:
        print("ennter the class room ")
        
        print(Fore.YELLOW + f" totale today persent student : {self.totale}\n{self.stud}")
        print(Fore.RED + f"total today appends student : {10-self.totale}" )
    def savefile(self):
        rollnumber=[self.n]
        with open("attends.file","a+") as f:
             save=f.write(f"DATE ::{str(datetime.date.today())}\n\t TIME::{str(time.strftime("%H:%M:%S"))} \n STUDENT::{str(self.student)}\n ROLL.NUMBER{str(rollnumber)}\n")
              
        
    def __str__(self):
       return("thank for today comming")
       
       
    



student=[] # list of student given input


i=1
totale =0
try :
           
          while True:
             n=int(input(Fore.BLUE + "enter the roll number:::"))
             m=input(Fore.BLUE +"enter the your name : ").lower()
             ad={}
             ad[n]=f"{m}"
      
             if n  in d and d[n]==m  :
                 print(Fore.GREEN + "enter the class room 🥰🥰🫡🫡")
                 print(Fore.CYAN+"next")
                 if  "12:00">=time.strftime("%H:%M")  or  i>10:
                     
                      student.append(m)
                      totale+=1

                      
                      a=attends(n,totale,student)
                      a.check()
                      a.savefile()
                     
                      i+=1
             
             elif "12:00"<=time.strftime("%H:%M") :
                  print("you are let ")
                  break
                      
                 
             elif m in student:
             
                 print("your toady   attends all ready have ")
                 print("thank you")
             else:
                 print( Fore.RED +    f"not your this class {m}  \n and you don't enter ❌❌ the this class room \n \t  thank you ")

                 
             
             
             
             i+=1
             
             
          
           
             
except Exception as e:
           print(e)
        



