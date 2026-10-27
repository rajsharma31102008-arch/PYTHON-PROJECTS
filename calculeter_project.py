

class calculeter:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
        
    def __add__(self):
         
         return f"sum of two number is :{(self.a)+(self.b)}"
    def __sub__(self):
           return f"sub of two number is :{(self.a)-(self.b)}"
    def __mul__(self):
           return f"mul of two number is:{(self.a)*(self.b)}"
    
    def __truediv__(self):
         return f"div of two number is :{(self.a)/(self.b)}"
     
try:
   while True:
       n=int(input("enter the number:"))
       m=int(input("enter the number:"))
       
       a=calculeter(n,m)

       print(a.__add__())
       print(a.__sub__())
       print(a.__mul__())
       print(a.__truediv__())
except Exception as e:
     print(e)
       



            
    
        
    
        