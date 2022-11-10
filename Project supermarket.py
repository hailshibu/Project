import mysql.connector as c
cnx=c.connect(host="localhost",user="root",password="SivaSarang",charset="utf8")
cur=cnx.cursor()
cur.execute("create database if not exists werehouse")
cur.execute("use werehouse")
cur.execute("CREATE TABLE IF NOT EXISTS items(itemnumber int, itemname varchar(50),quantity int ,MRP INT)")
cur.execute("CREATE TABLE IF NOT EXISTS employee(empno int, empname varchar(50),age int,emppost varchar(50), sal int,contact int)")
cur.execute("CREATE TABLE IF NOT EXISTS user_data(username varchar(45),password varchar(45))")
print("Welcome to SKG Werehouse management software")
while True:
  print("1)Login\n2)Register\n3)Exit")
  n=int(input("Enter your choice"))
  if n==3:
    print("Program closed")
    break
  elif n==2:
    u=input("Prefered user name")
    p=input("Enter prefered password")
    cur.execute("insert into user_data values('{}','{}')".format(u,p))
    cnx.commit()
    x=input("click on any key to continue")
    
  elif n==1:
    un=input("Enter user name").lower()
    p=input("Enter passcode")
    cur.execute("select password from user_data where username='{}'".format(un))
    pc=cur.fetchall()
    if cur.rowcount==0:
      print("User name not found")
    for i in pc:
      if str(i[0])==str(p):
        while True:
          print("\nMenu")
          print("1)Inventory\n2)Employee Details\n3)Order details\n4)Shipping details")
          a=int(input("Kindly Enter your choice"))
          if a==1:
            print("Stock details")
            print("1)Add new items")
            print("2)Remove items")
            print("3)modify item details")
            print("4)Search for items")
            print("5)Display all item details")
            print("6)Log out")
            b=int(input("Enter your choice"))
            if b==6:
              x=input("Enter any key to continue")
            elif b==1:
              k=int(input("Enter number of items to be added"))
              for i in range(k):
                    ino=int(input("Enter the item number"))
                    inm=input("Enter the item name")
                    qty=int(input("Enter the quantity to be added"))
                    mrp=int(input("Enter the price of the item"))
                    cur.execute("insert into items values({},'{}',{},{})".format(ino,inm,qty,mrp))
                    cnx.commit()
              print("Items added successfully")
            elif b==2:
              o=int(input("Enter number of items to delete"))
              for i in range(o):
                    print("1)Itemname\n OR\n2)Item number of the item to be deleted")
                    ch=int(input("Enter choice"))
                    if ch==1:
                          nm=input("Enter item name to delete")
                          cur.execute("delete from items where itemname='{}'".format(nm))
                          cnx.commit()
                    if ch==2:
                          no=int(input("Enter item number to delete"))
                          cur.execute("delete from items where itemnumber={}".format(no))
                          cnx.commit()
            elif b==3:
              n=input("Enter itemname of the item to modify")
              cur.execute("select * from items where itemname='{}'".format(n))
              c=cur.fetchall()
              print(c)
              for i in c:
                l=list(i)
                if l[1]==n:
                  ch=input("Change itemnumber?y/n")
                  if ch in "Yy":
                    l[0]=int(input("Enter new itemnumber"))
                  ch=input("Change itemname?y/n")
                  if ch in "Yy":
                    l[1]=input("Enter new itemname")
                  ch=input("Change quantity?y/n")
                  if ch in "Yy":
                    l[2]=int(input("Enter new quantity"))
                  ch=input("Change MRP?y/n")
                  if ch in "Yy":
                    l[3]=int(input("Enter new MRP"))
                cur.execute("UPDATE ITEMS SET ITEMNUMBER={},ITEMNAME='{}',QUANTITY={},MRP={} where ITEMNAME='{}'".format(l[0],l[1],l[2],l[3],n))
                cnx.commit()
            elif b==4:
              n=input("Name of the item to be searched")
              cur.execute("select * from items where itemname='{}'".format(n))
              c=list(cur.fetchone())
              print("Itemnumber","Itemname","Quantity","MRP",sep="\t")
              for i in c:
                print(i,end="        \t")
                
            elif b==5:
              cur.execute("select * from items")
              c=cur.fetchall()
              print("Itemnumber","Itemname","Quantity","MRP",sep="\t")
              k=[]
              for i in c:
                l=list(i)
                k.append(l)
              for j in k:
                print(j[0],j[1],j[2],j[3],sep="        \t")
              
            else:
              continue
          elif a==2:
            print("Employee details")
            print("1)Add new employee")
            print("2)Remove employee")
            print("3)modify employee details")
            print("4)Search for employee detail")
            print("5)Display all employee details")
            print("Log out")
            b=int(input("Enter your choice"))
            if b==6:
              x=input("Enter any key to continue")
            elif b==1:
              k=int(input("Enter number of employees to be added"))
              for i in range(k):
                    eno=int(input("Enter the employee number"))
                    emn=input("Enter the employee name")
                    age=int(input("Enter the age"))
                    pos=input("Enter the post name")
                    sal=int(input("Enter the Salary"))
                    con=int(input("Contact number"))
                    cur.execute("insert into employee values({},'{}',{},'{}',{},{})".format(eno,emn,age,pos,sal,con))
                    cnx.commit()
              print("Employee details added successfully")
            elif b==2:
              o=int(input("Enter number of employee to delete"))
              for i in range(o):
                    print("1)Employee name\n OR\n2)Employee number of the employee to be deleted")
                    ch=int(input("Enter choice"))
                    if ch==1:
                          nm=input("Enter employee name to delete")
                          cur.execute("delete from items where empname='{}'".format(nm))
                          cnx.commit()
                    if ch==2:
                          no=int(input("Enter employee number to delete"))
                          cur.execute("delete from employee where empno={}".format(no))
                          cnx.commit()
            elif b==3:
              n=input("Enter employee name of the emplyee to modify")
              cur.execute("select * from employee where empname='{}'".format(n))
              c=cur.fetchall()
              print(c)
              for i in c:
                l=list(i)
                if l[1]==n:
                  ch=input("Change employee number?y/n")
                  if ch in "Yy":
                    l[0]=int(input("Enter new employee number"))
                  ch=input("Change employee name?y/n")
                  if ch in "Yy":
                    l[1]=input("Enter new employee name")
                  ch=input("Change age?y/n")
                  if ch in "Yy":
                    l[2]=int(input("Enter new age"))
                  ch=input("Change post?y/n")
                  if ch in "Yy":
                    l[3]=input("Enter new post")
                  ch=input("Change salary?y/n")  
                  if ch in "Yy":
                    l[4]=int(input("Enter new salary"))
                  ch=input("Change contact number?y/n")
                  if ch in "Yy":
                    l[5]=int(input("Enter new contact number"))
                cur.execute("UPDATE EMPLOYEE SET EMPNO={},EMPNAME='{}',AGE={},emppost='{}',sal={},contact={} where EMPNAME='{}'".format(l[0],l[1],l[2],l[3],l[4],l[5],n))
                cnx.commit()
            elif b==4:
              n=input("Name of the employee to be searched")
              cur.execute("select * from employee where empname='{}'".format(n))
              c=list(cur.fetchone())
              print("Employee number","Employee name","Age","Post","Salary","Contact number",sep="\t")
              for i in c:
                print(i,end="        \t")
                
            elif b==5:
              cur.execute("select * from items")
              c=cur.fetchall()
              print("Itemnumber","Itemname","Quantity","MRP",sep="\t")
              k=[]
              for i in c:
                l=list(i)
                k.append(l)
              for j in k:
                print(j[0],j[1],j[2],j[3],j[4],j[5],sep="        \t")
              
            else:
              continue
            
           
             
                    
            
            
 
