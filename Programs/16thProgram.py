import mysql.connector as m
d=m.connect(host='localhost',user='root',password='mysql',database='hamza')
c=d.cursor()

def createtable():
    c.execute('create table product (p_id varchar(5),productname varchar(20),manufacturer varchar(3),price int, expirydate date);')

def insertdata():
    l=('TP01','Talcum Powder','LAK',40,'2011-06-26')
    m=('FW05','Face Wash','ABC',45,'2010-12-01')
    n=('BS01','Bath Soap','ABC',55,'2010-09-10')
    o=('SH06','Shampoo','XYZ',120,'2012-04-09')
    p=('FW12','Face Wash','XYZ',95,'2010-08-15')
    q="insert into product values(%s,%s,%s,%s,%s);"
    c.execute(q,l)
    c.execute(q,m)
    c.execute(q,n)
    c.execute(q,o)
    c.execute(q,p)


def display():
    c.execute('select * from product order by price desc;')
    a=c.fetchall()
    for i in a:
        print(i)

def update():
    c.execute('update product set price=price+(price*0.1);')


# createtable()
# insertdata()
# display()
# update()
d.commit()
d.close()