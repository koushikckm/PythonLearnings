i=1
def A():
    i=5
    print("I am the local i = ",i)
    def B():
        #nonlocal i
		i=7
        print("I am the nonlocal i = ",i)
        i=6
        print("I am the new i = ",i)
    B()
    
print("I am the global i = ",i)

A()