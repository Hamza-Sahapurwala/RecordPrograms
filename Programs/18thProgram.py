import mysql.connector as m
d=m.connect(host='localhost',user='root',password='mysql',database='hamza')
c=d.cursor()

def createtable():
    c.execute('create table company (cid int,companyname varchar(20),city varchar(10),productname varchar(20));')

def insertdata():
    l=(111,'Sony','Delhi','TV')
    m=(222,'Nokia','Mumbai','Mobile')
    n=(333,'Onida','Delhi','TV')
    o=(444,'Sony','Mumbai','Mobile')
    p=(555,'BlackBerry','Bangalore','Mobile')
    q="insert into company values(%s,%s,%s,%s);"
    c.execute(q,l)
    c.execute(q,m)
    c.execute(q,n)
    c.execute(q,o)
    c.execute(q,p)

def display():
    c.execute("select * from company where companyname like 'S%';")
    a=c.fetchall()
    for i in a:
        print(i)

def remove():
    c.execute("delete from company where productname='Mobile';")

# createtable()
# insertdata()
# display()
# remove()

d.commit()
d.close()