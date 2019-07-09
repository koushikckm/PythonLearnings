f=open("D:\\PYTHON\\workspace\\fileIO\\readbulk.txt")
lines=f.readlines()
f.close()

f=open("D:\\PYTHON\\workspace\\fileIO\\writebulk.txt","w")
f.writelines(lines)
f.close()