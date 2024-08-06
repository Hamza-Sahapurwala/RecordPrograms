import mysql.connector as m
d=m.connect(host='localhost',user='root',password='mysql',database='hamza')
c=d.cursor()

def createtable():
    c.execute('create table employee (e_id int,fname varchar(10),lname varchar(10),hire_date date, salary int);')

def insertdata():
    l=(102,'Amit','Mishra','1998-10-12',12000)
    m=(103,'Nitin','Vyas','1994-12-24',8000)
    n=(104,'Rakshit','Soni','2001-05-18',14000)
    o=(105,'Rashmi','Malhotra','2004-09-11',11000)
    p=(106,'Sunny','Gopal','2002-06-19',10000)
    q="insert into employee values(%s,%s,%s,%s,%s);"
    c.execute(q,l)
    c.execute(q,m)
    c.execute(q,n)
    c.execute(q,o)
    c.execute(q,p)

def display():
    c.execute('select e_id,fname,lname from employee where salary between 10000 and 14000;')
    a=c.fetchall()
    for i in a:
        print(i)

def total():
    c.execute('select sum(salary) from employee;')
    a=c.fetchall()
    for i in a:
        print(i)

createtable()
insertdata()
display()
total()

d.commit()
d.close()
    