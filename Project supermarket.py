import mysql.connector as c
cnx=c.connect(host="localhost",user="root",password="SivaSarang",charset="utf8")
cur=cnx.cursor()
cur.execute("create database if not exists werehouse")
cur.execute("use werehouse")
cur.execute("CREATE TABLE IF NOT EXISTS items(itemnumber int, itemname varchar(50),quantity int ,MRP INT)")
cur.execute("CREATE TABLE IF NOT EXISTS employee(empid int, empname varchar(50),emppost varchar(50), sal int)")
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
          print("Menu")
          print("1)Inventory\n2)Employee Details\n3)Customer Details\n4)Billing")
          a=int(input("Kindly Enter your choice"))
          if a==1:
            print("Stock details")
            print("1)Add new items")
            print("2)Remove items")
            print("3)modify item details")
            print("4)Search for items")
            print("5)Display all item details")
            print("Log out")
            b=int(input("Enter your choice"))
            if b==5:
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
             n
                  
                
           
             
                    
            
            
 
