import sqlite3
conn=sqlite3.connect('employee.db')
conn.execute("insert into employee values (1,'Ram',28,'Bengaluru',15000)")
conn.execute("insert into employee values (2,'Ajay',29,'Mumbai',25000)")
conn.execute("insert into employee values (3,'Jack',30,'Delhi',35000)")
conn.commit()
print("Records created successfully")
conn.close()