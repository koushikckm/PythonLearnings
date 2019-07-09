# file two.py
import one

print("****This is two.py****")

print("name is :"+__name__)

if __name__=="__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")

one.func()