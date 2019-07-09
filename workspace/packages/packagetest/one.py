# file one.py
from twopackage import two
from twopackage.threepackage import three

print("****This is one.py****")
print("name is :"+__name__)

two.twofunc()
three.threefunc()