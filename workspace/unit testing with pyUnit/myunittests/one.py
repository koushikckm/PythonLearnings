import re

def checkfunction1(num1, num2):
    if num1>num2:
        return True
    else:
        return False
    
def checkfunction2(strng):
    text=strng
    regex=re.compile('E.*y')
    matched=re.match(regex,text)
    if matched:
        return True
    else:
        return False