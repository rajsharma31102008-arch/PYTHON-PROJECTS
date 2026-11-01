#today project bank Management System
# bank name =  self-bank
#CREATED BY : RAJ SHARMA
from datetime import date, datetime
from colorama import Fore,init

init()
today=date.today() # today date
colors=(Fore.BLUE,Fore.GREEN,Fore.RED,Fore.MAGENTA,Fore.YELLOW)
print(Fore.YELLOW + ("-------------------------------------------------------------------------"))
print(colors[1] + ("--------------------self-bank--------------------------"))
print(Fore.YELLOW +"-------------------------------------------------------------------------")
import mysql.connector
dpp=mysql.connector.connect(
    host="localhost",
    user="root",
    password="user_password")
cur=dpp.cursor()
cur.execute("create database if not exists selfbank")
cur.execute("use selfbank")
class bank:
    def __init__(self,en=None,ea=None,eg=None,es=None,ed=None):
        self.en=en  #employee name =en
        self.ea=ea   # employee age=ea
        self.eg=eg   # employee gender=eg
        self.es=es   #employee salary=es
        self.ed=ed   # employee department =ed

     
    def employee (self): #bank employee table 
        cur.execute("use selfbank")
        cur.execute( """create table if not exists employee(
        id bigint auto_increment primary key,
        name varchar(234) not null,
        age int check(18<age<60) not null,
        gender varchar(25) not null,
        salary decimal(20,2),
        DEPARTMENT VARCHAR(200)
        );""")
        cur.execute("alter table employee auto_increment=40202601")
        cur.execute("alter table employee add joining_date date default(current_date);")
        cur.execute("alter table employee add joining_time time  default(current_time);") #insert the values all 👇
        cur.execute("insert into employee(name,age,gender,salary,DEPARTMENT) VALUES(%s,%s,%s,%s,%s)",((self.en),(self.ea),(self.eg),(self.es),(self.ed)))
        
    
class manager(bank):
    def __init__(self,):
        pass
    def managers(self):
         cur.execute("use selfbank")
         cur.execute("""create table if not exists managers (
         id varchar(234)  ,
         password varchar(24),
          constraint primary key (id,password) );""")
         cur.execute("insert into managers(id,password) values(%s,%s)",("raj9273","raj@7903"))
    @staticmethod
    def login(uu,up):
        cur.execute("use selfbank")
        cur.execute("""create table if not exists userlogin(
           id varchar(23),
           password varchar(24),
           constraint primary key (id,password))""")
        cur.execute("insert into userlogin(id,password) values(%s,%s)",(uu,up))
class customer(manager):
       def ___init___(self):
           pass
       def customertable(self):
           cur.execute("use selfbank")
           cur.execute("""create table if not exists customer(
           no int auto_increment,
           
           full_name varchar(234) not null ,
           age int check(18<=age) not null ,
           date_of_birth date unique not null,
           gender char(30) not null ,
           mobile_number bigint(20)  unique not null,
           email_id varchar(25)unique,
           father_name char(100) not null,
           mother_name char(100) not null
           address varchar(200) not null,
           city varchar(200) not null,
           state varchar(200) not null,
           pin_code bigint ,
           aadhar_number bigint  ,
           pan_number varchar(30),
           account_number bigint ,
           account_type varchar(234) default("account saving"),
           balance decimal(50,3) default(000),
           Branch varchar(100) not null,

           constraint primary key(no,aadhar_number,pan_number,account_number);          
           """)
           cur.execute("alter table customer add account_opening_date date default(current_date()) after no ;")
       @staticmethod
       def  dulcustomer(name,age,dio,gender,mobile,email,father,mother,addr,city,state,pin,aadhar,pan,account,balance,branch):
           cur.execute("use selfbank ")
           cur.execute("""insert into customer(full_name,age,date_of_birth,gender,mobile_number,email_id,
           father_name,mother_name,address,city,state,pin_code,aadhar_number,pan_number,account_number,
           balance,branch) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(name,age,dio,gender,mobile,email,father,mother,addr,city,state,pin,
                                                                                             aadhar,pan,account,balance,branch))     
       def inputcustomer(self):
           try:
              name=input("enter your full name :")
              age=int(input("enter your age :"))        
              dio=input("enter your date of birth :")
              gender=input("enter your gender :")
              mobile=input("enter your mobile number :")
              email=input("enter your email id :")
              father=input("enter your father's name :")
              mother=input("enter your mother's name :")
              addr=input("enter your address :")
              city=input("enter your city :")
              state=input("enter your state :")
              pin=int(input("enter your pin code :"))
              aadhar=int(input("enter your aadhar number :"))
              pan=input("enter your pan number :")
              account=int(input("enter your account number :"))
              balance=int(input("enter your balance :"))
              branch=input("enter your branch :")

              customer.dulcustomer(name,age,dio,gender,mobile,email,father,mother,addr,city,state,pin,aadhar,pan,account,balance,branch)       
               
           except Exception as e:
               print(e)
           
                 
try:    
    while True:
        print("DATE:",today)
        print("TIME:",datetime.now().strftime("%H:%M:%S"))
        print(Fore.CYAN +    "-----login-----")
        user=input("enter your username id :")
        password=input("enter your password :")
        cur.execute("use selfbank")
        cur.execute("select*from userlogin where id=%s and password=%s;",(user,password))
        d=cur.fetchone()
        cur.execute("select*from managers where id=%s and password=%s ;",(user,password))
        m=cur.fetchone()
        if d:
             print(Fore.GREEN +"login successfully")
             customer().inputcustomer()
             try:
                  num=input(Fore.BLUE +"you udate the customer table say (yes/no):\nyou update phone number say (pn):\nyou delete record say (de):\n:").lower()
                  
                  if num=="pn":
                       try:
                        update=input(Fore.BLUE+"enter the account number")
                        number=int(input("enter you phone number is :"))
                        cur.execute("use selfbank")
                        cur.execute(f"update customer set mobile_number={number} where account_number={update} ")
                        dpp.commit()
                        
                       except Exception as e:
                           print(e)
                       finally:
                           print("update successfully")
                  elif num=="de":
                      try:
                        delete=input("enter the account number :").lower()
                        cur.execute("use selfbank")
                        cur.execute(f"delete from customer where account_number={delete} ")
                        dpp.commit()
                      except Exception as e:
                          print(e)
                      finally:
                          print("delete successfully")
                  elif num=="yes":
                    try:
                       check=input("what do you want Deposit/Withdraw :").lower()
                       if check=="deposit":
                           try:
                            account=int(input("enter your account number :"))
                            amount=int(input("enter your deposit amount :"))
                            cur.execute("use selfbank")
                            cur.execute(f"update customer set balance=balance+{amount} where account_number={account}")
                            cur.execute("select*from customer where account_number=%s",(account))
                            fet=cur.fetchall()
                            print(fet)
                            dpp.commit()

                           except Exception as e:
                               print(e)
                           finally:
                                print("deposit successfully")
                       elif check=="withdraw":
                              try:
                                account=int(input("enter your account number :"))
                                amount=int(input("enter your withdraw amount :"))
                                cur.execute("use selfbank")
                                cur.execute(f"update customer set balance=balance-{amount} where account_number={account}")
                                cur.execute("select*from customer where account_number=%s",(account))
                                fet=cur.fetchall()
                                print(fet)
                                dpp.commit()
                              except Exception as e:
                                  print(e)
                              finally:
                                  print("withdraw successfully")
                       else:
                           print(Fore.RED + "none")
                           break
                  
                        
                    except Exception as e:
                        print(e)
                    finally:
                        print("done")
                  else:
                   print(Fore.RED + "none")
                   break
             except Exception as p:
                  print(p)    
             finally :
                  print(Fore.CYAN +"done") 
        elif m:
            print(Fore.GREEN +"login successfully")
            print(Fore.BLUE +"what are you do it employee add (enter)= eadd \n employee check table (enter) = etable \n new customer add (enter)=cadd \n check customer (emter)=ctable")
            try:  
             w=input(Fore.YELLOW + "enter::::").lower()
            except Exception as e:
             print(e)
             if w=="eadd":
                try:
                   add=input("how many add the employee user/passower(up):\n add new employee table (et):").lower()
                   if add=="up":
                    try:
                     num=int(input(Fore.BLUE + "how many you add employee  :"))
                     print(e)
                     i=1
                     while i<=num:
                     
                          print(Fore.RED + "you must be used the hard password and user name 🧐🧐")
                          euser=input("enter the user name :")
                          epassword=input("enter the password :")
                          l=manager()
                          l.login(euser,epassword)
                          dpp.commit()
                          i+=1
                    except Exception as e:
                      print(e)
                   elif add=="et":
                    try:
                        num=int(input(Fore.BLUE + "how many you add employee  :"))
                        print(e)
                        i=1
                        while i<=num:
                            en=input("enter the employee name :")
                            ea=int(input("enter the employee age :"))
                            eg=input("enter the employee gender :")
                            es=int(input("enter the employee salary :"))
                            ed=input("enter the employee department :")
                            b=bank(en,ea,eg,es,ed)
                            b.employee()
                            dpp.commit()
                            i+=1
                    except Exception as e:
                        print(e)
                   else:
                    print(Fore.RED + "none")
                    break
                except Exception as e:
                         print(e)
                finally:
                    print("done")
             elif w=="etable":
                try:  
                 num=input(Fore.BLUE + "how many you check it one /all  :\n \n delete (de)").lower()
                except Exception as e :
                 print(e)
                 if num=="all":
                     cur.execute("use selfbank")
                     cur.execute("select*from employee;")
                     fet=cur.fetchall()
                     print(fet)
                     break
                 elif num=="one":
                    try:
                     sid=input(Fore.CYAN + "where you employee see table \n enter the id::").lower()
                   
                     cur.execute("use selfbank")
                     cur.execute("select*from employee where id=%s",(sid))
                     sidc=cur.fetchall()
                     print(sidc)
                     break
                    except Exception as e:
                        print(e)
                    finally:
                        print("done")
                 
                     
                 elif num=="de":
                     try:
                        delete=input("enter the employee id :").lower()
                        cur.execute("use selfbank")
                        cur.execute("delete from employee where id=%s ",(delete))
                        dpp.commit()
                     except Exception as e:
                         print(e)
                     finally:
                         print("delete successfully")               
                 else:
                     print(Fore.RED + "none")
                     break
             elif w=="cadd":
                 check=input(Fore.BLUE + "you add new customer (add):\n delete customer (de):").lower()
                 if check=="de":
                     try:
                        delete=input("enter the account number :").lower()
                        cur.execute("use selfbank")
                        cur.execute("delete from customer where account_number=%s",(delete))
                        dpp.commit()
                     except Exception as e:
                         print(e)
                     finally:
                         print("delete successfully")
                 elif check=="add":
                    try:
                         add=int(input(Fore.BLUE + "how many you add customer  :"))
                         i=1
                         while i<=add:
                             customer().inputcustomer()
                             i+=1
                    except Exception as e:
                        print(e)
                    finally:
                        print("done")
                 else:
                     print(Fore.RED + "none")
                     break
             elif w=="ctable":
                 try:
                     num=input(Fore.BLUE + "how many you check it one /all ::").lower()
                 except Exception as e :
                     print(e)
                 if num=="all":
                     cur.execute("use selfbank")
                     cur.execute("select*from customer;")
                     fet=cur.fetchall()
                     print(fet)
                     break
                 elif num=="one":
                    try:
                     sid=input(Fore.CYAN + "where you employee see table \n enter the id::").lower()
                   
                     cur.execute("use selfbank")
                     cur.execute("select*from customer where no=%s",(sid))
                     sidc=cur.fetchall()
                     print(sidc)
                     break
                    except Exception as e:
                                          print(e)
                         
                 else:
                    print(Fore.RED + "none")
                    break

            
             else:
                print(Fore.RED +"somthing ☠️☠️☠️☠️ wrong ❌❌❌❌❌❌❌")
        else:
            print(Fore.RED +"Invalid Username or Password")

except Ellipsis as e:
    print(Fore.RED + "error")
finally:
    print(Fore.CYAN + "done")


dpp.commit()