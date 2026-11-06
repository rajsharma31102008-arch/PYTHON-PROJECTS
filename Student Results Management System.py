
# student results management system


import pandas as pd
import mysql.connector
from datetime import date, datetime
from colorama import Fore,Style ,init
init()
today=date.today()
print(Style.BRIGHT + Fore.GREEN + "Connecting to MySQL Database..." + Style.RESET_ALL)

dpp=mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)
cur=dpp.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS  results")
cur.execute("USE results")

class pandas_to_mysql: #excel to mysql
      def __init__(self):
               pass
      def listsum(self):
           cur.execute("use results")
           sd=pd.read_sql("select*from student",dpp)
           sd.to_excel("student.xlsx",index=False)
      def excel_to_mysql(self):
         cur.execute("use results")
        #  sedt=cur.execute("select*from teacher")
         sd=pd.read_sql("select*from teacher", dpp)
         sd.to_excel("teacher.xlsx", index=False)
         dpp.commit()
        
class MySQLDatabase :#id/password table create this teacher / and student table create rollcode and rollnumber!!!!

     def __init__(self):
            pass
     def table(self):
         cur.execute("use results")
         cur.execute("""create table  if not exists teacher(
         date date default(current_date),
         time time default(current_time),
         no int auto_increment ,
         id varchar(34) unique not null,
         password varchar(24) unique not null,
         name varchar(56) not null,
         age int check(age>=18 and age<60) not null,
         bio  date  default(current_date) ,
          gender varchar(25) default("other"),
          department varchar(100) not null,
          constraint primary key (no));""")
         
         self.pandasto()
         dpp.commit()
     def pandasto(self):
           pandas_to_mysql().excel_to_mysql()
     def student_table(self):
         cur.execute("use results")
         cur.execute("""create table if not exists student(
         reg bigint auto_increment unique ,
         school varchar(250) default("UPGARDED +2 HIGH SCHOOL SIMULDANGA JAMSHEDPUR 1"),
         roll_number int ,
         roll_code int ,
        
           name char(50) not null,
            father_name char(50) not null,
             mother_name char(50) not null ,
               date_of_birth date not null,
               photo varchar(200) not null,
               english int check(english>=0 and english<=100) not null ,
               math int check(math>=0 and math<=100) not null,
               history int check(history>=0 and history<=100) not null,
                  auto_motive int check(auto_motive>=0 and auto_motive<=100),
                    science int check(science>=0 and science<=100),
                      hindi int check(hindi>=0 and hindi<=100),
                       totale int check(totale>0 and totale<=500) ,
                       Percentage decimal(10,2) check(percentage>=0 and Percentage<=100 ),
                 constraint primary key  (roll_number,roll_code ) );""")
         cur.execute("alter table student auto_increment=0001")
         dpp.commit()
ps=MySQLDatabase()

ps.student_table()
ps.table()
         
def studen(q,w,e,r,t,y,u,i,o,p,a,s,d,f,g):
     cur.execute("use results")    #insrt table student
     cur.execute("""insert into student (roll_code,roll_number,name,father_name,mother_name,date_of_birth,
     photo ,english,math,history,auto_motive,science,hindi,totale,Percentage ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""",(q,w,e,r,t,y,u,i,o,p,a,s,d,f,g))
     dpp.commit()
     pandas_to_mysql().listsum()
     
def markinput(): # input student mark and all 
      
      try:
           while True:
                
                q=int(input(Style.BRIGHT + Fore.BLUE +F"enter the roll code :\n::"))
                w=int(input(Style.BRIGHT + Fore.CYAN + f"enter the roll number:\n::"))
                e=input(Style.BRIGHT + Fore.BLUE + f"enter the name :\n::")
                r=input(Style.BRIGHT + Fore.CYAN + f"enter the father name:\n::")
                t=input(Style.BRIGHT + Fore.BLUE + f"enter the mother name :\n::")
                y=input(Style.BRIGHT + Fore.CYAN + f"enter the date of birth  write on (y-m-d):\n::")
                u=input(Style.BRIGHT + Fore.BLUE + f"uplode the photo :\n::")
                i=int(input(Style.BRIGHT + Fore.CYAN + f"enter the mark of english:\n::"))
                
                o=int(input(Style.BRIGHT + Fore.BLUE + f"enter the mark of math :\n::"))
                p=int(input(Style.BRIGHT + Fore.CYAN + f"enter the mark of history :\n::"))
                a=int(input(Style.BRIGHT + Fore.BLUE + f"enter the mark of auto motive :\n::"))
                s=int(input(Style.BRIGHT + Fore.CYAN + f"enter the mark of science :\n::"))
                d=int(input(Style.BRIGHT + Fore.BLUE + f"enter the mark of hindi:\n::"))
                if i>=o and p>=o and a>=o and s>=o and d>=o:
                    try:
                     lists=[]
                     lists.extend([i,p,a,s,d])
                     f=sum(lists)
                     g=(i+p+a+s+d)/5
                     studen(q,w,e,r,t,y,u,i,o,p,a,s,d,f,g)
                    except ValueError as e:
                          print(Style.DIM + Fore.RED + f"error{e}")
                elif o>=i and p>=i and  a>=i and d>=i and s>=i:
                     try:
                          lists=[]
                          lists.extend([o,p,a,s,d])
                          f=sum(lists)
                          g=(o+p+a+d+s)/5
                          studen(q,w,e,r,t,y,u,i,o,p,a,s,d,f,g)
                     except ValueError as e:
                           print(Style.DIM + Fore.RED + f"error{e}")
                elif o>=p and s>=p and a>=p and d>=p  and i>=p:
                     try:
                       lists=[]
                       lists.extend([o,i,a,s,d])
                       f=sum(lists)
                       g=(o+i+a+d+s)/5
                       studen(q,w,e,r,t,y,u,i,o,p,a,s,d,f,g)
                     except ValueError as e:
                             print(Style.DIM + Fore.RED + f"error{e}")
                elif o>=a and p>=a and s>=a and d>=a and i>=a:
                 try:
                     lists=[]
                     lists.extend([o,p,i,s,d])
                     f=sum(lists)
                     g=(o+p+i+d+s)/5
                     studen(q,w,e,r,t,y,u,i,o,p,a,s,d,f,g)
                 except ValueError as e:
                        print(Style.DIM + Fore.RED + f"error{e}")
                elif o>=s and p>=s and i>=s and d>=s  and a>=s:
                     try:
                        lists=[]
                        lists.extend([o,p,a,i,d])
                        f=sum(lists)
                        g=(o+p+a+d+i)/5
                        studen(q,w,e,r,t,y,u,i,o,p,a,s,d,f,g)
                     except ValueError as e:
                          print(Style.DIM + Fore.RED + f"error{e}")
                else:
                     try:
                        lists=[]
                        lists.extend([o,p,a,s,i])
                        f=sum(lists)
                        g=(o+p+a+i+s)/5
                        studen(q,w,e,r,t,y,u,i,o,p,a,s,d,f,g)
                     except ValueError as e:
                       print(Style.DIM + Fore.RED + f"error{e}")

      except Exception as e:
           print(Style.DIM + Fore.RED + f"error{e}")
def alter():
     try:
       rollnumber=int(input(Style.BRIGHT+Fore.GREEN+ "enter the roll number:\n::"))
       rollcode=int(input(Style.BRIGHT+Fore.CYAN+ "enter the roll number:\n::"))
         #student enter the roll number and roll code its self 
       cur.execute("use results")
       cur.execute("select*from student where roll_number=%s and roll_code=%s",(rollnumber,rollcode))
       data=cur.fetchone()
       if data:
           print(Style.BRIGHT+Fore.GREEN+"login succes")
       else:
           print(Style.NORMAL+Fore.RED +"invalid roll number or roll code ")
     except Exception as e:
           print(Style.DIM + Fore.RED + f"error{e}")

def teac():
     try:
         idp=input(Style.BRIGHT + Fore.BLUE + "enter the you id : \n::")
         password=input(Style.DIM + Fore.GREEN + "enter the password :\n::")
         cur.execute("use results")
         cur.execute("select id ,password from teacher where id=%s and password=%s",(idp,password))
         data=cur.fetchone()
         if data :
              print( Style.BRIGHT+Fore.GREEN+"login succes")
              try: #teacher input
                           sets=input(" you add new or old update enter(new/update)")
                           if sets=="new":
                              markinput() # function of student of mark input
                           elif sets=="update":
                               stud()
                           else:
                               print(Fore.RED+"somthing wrong try agin !!")
                               teac()
              except Exception as e:
                  print( Style.BRIGHT + Fore.RED  ,e )
         else:
              print(Style.NORMAL + Fore.RED + " id/ password wrong !!!")
     except Exception as e:
          print( Style.BRIGHT + Fore.RED  ,e )
     
     
def stud():
  try:
     s = ["name", "father_name", "mother_name", "date_of_birth",
     "photo", "english", "math", "history", "auto_motive",
     "science", "hindi", "totale", "Percentage"]

     print(Style.BRIGHT + Fore.MAGENTA + "Available columns:", s)

     columnname=input(Style.DIM + Fore.GREEN +"which column update you :\n::").lower()
     value=input(Style.DIM + Fore.CYAN +"update the row :\n::").lower()
     rollnumber=int(input(Style.NORMAL + Fore.BLUE +"enter the rollnumber :\n::"))
     rollcode=int(input(Style.NORMAL+Fore.CYAN +"enter the rollcode"))
     

     if columnname not in s:
        print(Fore.RED+"invaild column name ")
     else: 
            cur.execute("use results")
            quit=(f"update student set {columnname}=%s where roll_number=%s and roll_code=%s ")
            cur.execute(quit,(value,rollnumber,rollcode))
            dpp.commit()
            pandas_to_mysql().listsum()
     
  except Exception as e:
      print(Style.BRIGHT + Fore.RED + f"error{e}")
  
     
try:  
  while True:
    print(today)
    print(datetime.now().strftime("%H:%M:%S"))
    none=input("who are you? teacher or student : ").lower()
    if none=="teacher":
         print( Style.BRIGHT + Fore.BLUE + "login as teacher" + Style.RESET_ALL)

         teac()
    elif none=="student":
         print( Style.BRIGHT + Fore.BLUE + "login as student" + Style.RESET_ALL)
         alter()
    else:
         
         print( Style.BRIGHT + Fore.RED + "invalid input" + Style.RESET_ALL)
         
except Exception as e:
    print(e)
#done project--- 