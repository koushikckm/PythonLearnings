import sqlite3
conn=sqlite3.connect('employee.db')
cursor=conn.execute("select id,name,address,salary from employee")
for row in cursor:
    print("ID = ",row[0])
    print("Name = ",row[1])
    print("Address = ",row[2])
    print("Salary = ",row[3])
    
print("Operation successful")

print("Updating row...")
conn.execute("update employee set salary=50000 where id=3")

print("After updating")
cursor=conn.execute("select id,name,address,salary from employee")
for row in cursor:
    print("ID = ",row[0])
    print("Name = ",row[1])
    print("Address = ",row[2])
    print("Salary = ",row[3])

conn.close()