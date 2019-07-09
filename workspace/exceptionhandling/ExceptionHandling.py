try:
    5/0
except ZeroDivisionError:
    print("Please do not divide by 0")
	

r=100
try:
    print("Money"+r+"Available")
except TypeError:
    print("This gives a TypeError")
	
	
k=int(input("Please enter an integer"))
try:
    j=10/k
    print("Congratulations! Your result is ",j)
except:
    print("Div by 0 error")
finally:
    print("thank you")
	
	
file_name="chunckfile.txt"
text=[]
try:
    fh=open(file_name,'r')
except IOError:
    print("Cannot open ",file_name)
else:
    text=fh.readlines()
    fh.close()
    
if text:
    print(text)