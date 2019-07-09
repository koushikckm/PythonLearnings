class MyBaseClass(): 
    def __init__(self, var1):
        self.__myprivatevar = var1
        
class InheritedClass(MyBaseClass): 
    def __init__(self): 
        #Your code
        super().__init__(setmyprivatevar)


class Error(Exception):
   pass

class SmallNumber(Error):
    def raiseexception(self):
        print("Hi, you are inside SmallNumber Class")

class LargeNumber(Error):
    def raiseexception(self):
        print("Hi, you are inside LargeNumber Class")

number = 15


while True:
   try:
       num = int(input("Enter a number: "))
       if num < number:
           raise SmallNumber
       elif num > number:
           raise LargeNumber
       break
   except SmallNumber:
    print("This value is too small, try again!")
    k = SmallNumber()
    k.raiseexception()
   except LargeNumber:
    k = LargeNumber()
    k.raiseexception()
    print("This value is too large, try again!")
print("Congratulations! Your guess is right.")