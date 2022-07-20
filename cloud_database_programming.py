from ast import main
from unittest import result
import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(host="bogece8nvrhk1hzip6fg-mysql.services.clever-cloud.com", 
                            user = "usbbhub0o6aw4yvb", 
                            password = "RzOUmpM27zYIYTm9ZEp7",
                            database = "bogece8nvrhk1hzip6fg" )

def add_mobile():
    curs = con.cursor(prepared=True)

    prod_id = input("Enter Product key :")
    model_name = input("Enter Model Name :")
    company = input("Enter Comapny Name :")
    connectivity = input("Enter Connectivity type (4G/5G) :")
    ram = input("Enter RAM :")
    rom = input("Enter ROM :")
    color = input("Enter Color :")
    screen = input("Enter Screen type :")
    battery = input("Enter battery capacity :")
    processor = input("Enter name of processor :")
    price = input("Enter Price of mobile :")
    rating = input("Enter rating of mobile :")

    query = """INSERT INTO `MOBILES`(`prodid`, `modelname`, `company`, `connectivity`, `ram`, `rom`, `color`, `screen`, `battery`, `processor`, `price`, `rating`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    
    b1 = (prod_id,model_name,company,connectivity,ram,rom,color,screen,battery,processor,price,rating)
    # print('b1 :',b1,type(b1))
    
    curs.execute(query,b1)

    con.commit()
# add_mobile()


def list_of_all_mobiles():
    curs = con.cursor()
    curs.execute("SELECT * FROM MOBILES")
    result = curs.fetchall()
    print(result)

    # create header
    head = ['prodid', 'modelname', 'company', 'connectivity', 'ram', 'rom', 'color', 'screen', 'battery', 'processor', 'price', 'rating']

    # display table
    print(tabulate(result, headers=head, tablefmt="grid"))
#list_of_all_mobiles()


def search_by_modelName():
    search_model = input("Enter Model Name")

    curs = con.cursor()
    query = "SELECT * FROM MOBILES WHERE modelname = %s"
    # curs.execute(query,(search_model))
    curs.execute("SELECT * FROM MOBILES WHERE modelname ='"+search_model+"'")

    result = curs.fetchall()
    if (len(result)==0):
        print('not found')
    else:
    # create header
        head = ['prodid', 'modelname', 'company', 'connectivity', 'ram', 'rom', 'color', 'screen', 'battery', 'processor', 'price', 'rating']
    
    # display table
        print(tabulate(result, headers=head, tablefmt="grid"))
#search_by_modelName()


def ascending_order():
    company_name= input("Enter name of company: ")
    curs = con.cursor()
    curs.execute("SELECT * FROM MOBILES WHERE company = '"+company_name+"' ORDER BY price")

    result = curs.fetchall()
    if (len(result)==0):
        print('not found')
    else:
    # create header
        head = ['prodid', 'modelname', 'company', 'connectivity', 'ram', 'rom', 'color', 'screen', 'battery', 'processor', 'price', 'rating']
    
    # display table
        print(tabulate(result, headers=head, tablefmt="grid"))
#ascending_order()


def update_price():
    product_id= input("Enter Product ID : ")
    new_price= input("Enter new price : ")

    curs= con.cursor(prepared=True)
    try:
    # query = "UPDATE MOBILES SET price = %s WHERE prodid = %s"
        curs.execute("UPDATE MOBILES SET price= "+new_price+ "WHERE prodid='"+product_id+"'")
    # curs.execute(query,(new_price,product_id))
        con.commit()
        print('Price Updated Successfully')

    except:
         print('mobile does not exist')
# update_price()


def delete():
    product_id = input("Enter Product ID : ")

    curs = con.cursor()
    query = "SELECT * FROM MOBILES WHERE prodid = %s"
    curs.execute("SELECT * FROM MOBILES WHERE  prodid ='"+product_id+"'")

    result = curs.fetchall()
    # create header
    head = ['prodid', 'modelname', 'company', 'connectivity', 'ram', 'rom', 'color', 'screen', 'battery', 'processor', 'price', 'rating']
    
    # display table
    print(tabulate(result, headers=head, tablefmt="grid"))
    que= input("Do you want to delete? (yes/no)")
    if que == 'yes':
        curs.execute("DELETE FROM MOBILES WHERE prodid= '" +product_id+"'")
        con.commit()
    else:
        pass
# delete()


def ram_rom():
    ram= input("Enter RAM: ")
    rom= input("Enter ROM: ")

    curs= con.cursor()
    query = "SELECT * FROM MOBILES WHERE ram = %s AND rom = %s"
    curs.execute("SELECT * FROM MOBILES WHERE ram ='"+ram+"'AND rom = '"+rom+"'")
    result = curs.fetchall()
    print(result)

    # create header
    head = ['prodid', 'modelname', 'company', 'connectivity', 'ram', 'rom', 'color', 'screen', 'battery', 'processor', 'price', 'rating']
   
    # display table
    print(tabulate(result, headers=head, tablefmt="grid"))
# ram_rom()


def add_column():
    curs= con.cursor(prepared = True)
    curs.execute("ALTER TABLE MOBILES ADD purpose varchar(50)")
    con.commit()
# add_column()


def update_all():
    model_name= input("Enter Model name: ")
    purpose= input("Enter the Purpose: ")
    curs= con.cursor(prepared= True)
    curs.execute("UPDATE MOBILES SET purpose= '"+purpose+"' WHERE modelname ='"+model_name+"'")
    con.commit()
# update_all()

def driver():
    while True:
        print("Welcome User! \n Enter choice of operation you want to perform.")
        print("1. Add Mobile in database")
        print("2. Display Database")
        print("3. Search Mobile by model name")
        print("4. Company wise mobiles with ascending prices")
        print("5. Update price with prodid")
        print("6. Delete mobile by prodid")
        print("7. Display mobiles with ram rom combination")
        print("8. Update all")
        print("9. exit")
        print("*"*20)
        choice = input("Enter the choice : ")

        if choice == "1":
            add_mobile()
        elif choice == "2":
            list_of_all_mobiles()
        elif choice == "3":
            search_by_modelName()
        elif choice == "4":
            ascending_order()
        elif choice == "5":
            update_price()
        elif choice == "6":
            delete()
        elif choice == "7":
            ram_rom()
        elif choice == "8":
            update_all()
        else:
            exit()


if __name__ == "__main__": 
    driver()
