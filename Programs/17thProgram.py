import mysql.connector as m
d=m.connect(host='localhost',user='root',password='mysql',database='hamza')
c=d.cursor()

def createtable():
    c.execute('create table stationary (s_id varchar(5),stationaryname varchar(20),comapany varchar(3),price int, stockdate date);')

def insertdata():
    l=('DP01','Dot Pen','ABC',10,'2011-03-31')
    m=('PL02','Pencil','XYZ',6,'2010-01-01')
    n=('ER05','Eraser','XYZ',7,'2010-02-14')
    o=('PL01','Pencil','CAM',5,'2009-01-09')
    p=('GP02','Gel Pen','ABC',15,'2009-03-19')
    q="insert into stationary values(%s,%s,%s,%s,%s);"
    c.execute(q,l)
    c.execute(q,m)
    c.execute(q,n)
    c.execute(q,o)
    c.execute(q,p)

def update():
    c.execute('update stationary set price=price+2;')

def display():
    c.execute("select * from stationery where company='XYZ';")
    a=c.fetchall()
    for i in a:
        print(i)

# createtable()
# insertdata()
# update()
# display()
d.commit()
d.close()