import mysql.connector
#create database
dpp=mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password")
cur=dpp.cursor()
cur.execute("create database if not exists   NSU;")
cur.execute("use NSU")

class student:   # student delite table
    def __init__(self,name=None ,age=None   , father =None  ,mother=None,fees=None   ,m =None):
        self.name=name
        self.father=father
        self.mother=mother
        self.age=age
        self.fees=fees
        self.m=m

        
        
    def student_table(self):
        cur.execute("use NSU")
        cur.execute("""create table  if   not exists    student(
        No int auto_increment primary key,
           date date default(current_date),
           time time default(current_time)  ,
                     
                     reg int  default(00) unique,
                     name varchar(233) not null,
                     age int ,
                     father_name varchar(233) not null,
                     mother_name varchar(56) default("unkown"),

                     fees decimal(20,2) default(0000));



                      """)
        cur.execute("insert into student(name,age,father_name,mother_name,fees) values(%s,%s,%s,%s,%s)",(self.name,self.age,self.father,self.mother,self.fees))
    def check(self):
        cur.execute ("select*from student")
        student=cur.fetchall()
        print(student)

    def studcheck(self):
        cur.execute("select * from student where    No = (select no from user where  id=%s) ",(self.m,  ))
        ds=cur.fetchall()
        print(ds)
    
        
        




class teacher    :
    def __init__(self,n,m):
        self.n=n
        self.m=m
        
    def usercheck(self):#student id and password table
         cur.execute("use NSU")
         cur.execute("""create table if not exists user(
         no int auto_increment,
         id varchar(10) ,
         password varchar(24),
          constraint primary key (id,password,no)); """)
         cur.execute("insert into user(id,password  ) values(%s ,%s)",(self.m,self.n ,))  
    def faculty(self):
         cur.execute(""""  create table   if  not   exists faculty(
                     No int auto_increment,
                     id varchar(10),
                    password varchar(24),
                    constraint primary key(id,password));
                      """)
         cur.execute("""    insert into faculty (id,password) values(%s,%s  ) 
                    """,   (   9952,"rishi sharma"))
                        
                            
         
          
try:
    
    while True:
        print("login")

        
        m=(input("ENTER THE USERNAME:"))
        n=(input("ENTER THE PASSWORD:"))
        cur.execute(" USE NSU ")

        
        cur.execute("select id, password from user")
        user=cur.fetchall()
        cur.execute("select id , password   from faculty")
        
        faculty=cur.fetchall()

        
        if (m,n) in user:
             
             print("student login")
             print(m)
             d=student(m=m  )
             d.studcheck()
             
             
        elif  (m,n)in faculty:
             print("faculty login")
             print(m)
             print("if check the student enter the dilute  \n\r and you add the student then  enter the add")
             work=input("enter the how do it you:").lower()

             if work=="add":
                try:
                 count=int(input("how many student add you:"))
                 i=1
                 while i  <=count:
                     print("you add is Complete  then enter the id = done")
                     
                     
                     id=input("enter the student user name ").lower()
                     print("you must we hard password create")
                     print("you add is Complete")
                     password=input("create the password")

                     t=teacher(id,password)
                     t.usercheck()
                     ze=input("you feel the student dilute:").lower()
                     if ze=="yes":
                         try:
                             s4=input("NAME:")
                             s5=int(input("AGE"))
                             s6=input("FATHER NAME:")
                             s7=input("MOTHER NAME:")
                             s8=int(input("FEEL"))
                             stud=student(s4,s5,s6,s7,s8)
                             stud.student_table()

                         except Exception as h:
                             print(h)
                     else:
                         break
                             
                     i+=1
             
                     
             
                except Exception as p:
                  print(p)
             elif work=="dilute":
                 s1=student()
                 s1.check()
             else:
                 break             
        else:
             print("something incorrect")

        
             
        

except Exception as e:
        print("error")
dpp.commit()