
import pymysql.cursors

conn=pymysql.connect(
    host="localhost",
    user="root",
    password="kavi8248",
    database="shopping"
    
)

cursor=conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS admin(
               ID INT PRIMARY KEY,
               Name varchar(100),
               Password BIGINT
               
    )
""")


def add_dish(ID,Dish_Name,Restaurant_Name,Ratings,Price):
    query="INSERT INTO food(ID,Dish_Name,Restaurant_Name,Ratings,Price) values(%s,%s,%s,%s,%s)"
    values=(ID,Dish_Name,Restaurant_Name,Ratings,Price)
    cursor.execute(query,values)
    conn.commit()
    


def view_dish():
    cursor.execute("SELECT * FROM food")
    dishes=cursor.fetchall()
    for dish in dishes:
        print(dish)

def update_dish(ID,Dish_Name,Restaurant_Name,Ratings,Price):
    query="UPDATE food SET Dish_Name=%s,Restaurant_Name=%s,Ratings%s,Price=%s WHERE ID=%s"
    values=(ID,Dish_Name,Restaurant_Name,Ratings,Price)
    cursor.execute(query,values)
    conn.commit()
    

def delete_dish(ID):
    query = "DELETE FROM food WHERE id = %s"
    values=("ID")
    cursor.execute(query,values)
    conn.commit()
   



def user():
    query="INSERT INTO admin(ID,Name,Password) values(%s,%s,%s)"
    values=(12,'kavi',8248)
    cursor.execute(query,values)
    conn.commit()



while True:

    try:
        ID=int(input("Enter Your ID:"))
        Name=input("Enter Your Name:")
        Password=int(input("Enter Your Password:"))


        query="SELECT * FROM admin WHERE ID=%s AND Name=%s AND Password=%s"
        cursor.execute(query,(ID,Name,Password))
        login=cursor.fetchone()
    

        if login  :
            print("Login Successfull.Welcome,",Name)

        else:
            print("Login Failed! Please Try again.")
            
            

    except:
        print("Error occured.")
        

    
    choice=input("Enter your choice (add/view/update/delete/customer/transaction/order details) in lower case:")

    if choice=="add":
        try:

            ID = int(input("Enter Dish ID:"))
            Dish_Name=input("Enter Dish Name:")
            Restaurant_Name=input("Enter Restaurant Name:")
            Ratings=float(input("Enter Ratings:"))
            Price=float(input("Enter price"))


            add_dish(ID, Dish_Name, Restaurant_Name, Ratings, Price)

            print("Added successfully")

        except:
            print("No Dishes Added")

    elif choice=="view":
        
        try:
            view_dish()

            

            print("viewed successfully")

        except:
            print("Not Viewed")

    elif choice=="update":

        try:
            
            ID = int(input("Enter Dish ID:"))
            Dish_Name=input("Enter Dish Name:")
            Restaurant_Name=input("Enter Restaurant Name:")
            Ratings=float(input("Enter Ratings:"))
            Price=float(input("Enter price"))

            update_dish(ID,Dsh_Name,Restaurant_Name,Ratings,Price)

            print("updated successfully")

        except:
            print("No Dishes Updated")

    elif choice=="delete":

        try:

            ID=int(input("Enter Dish ID to Delete:"))
            delete_food(ID)

            print("Deleted successfully")

        except:

            print("NO Dishes Deleted")
            

    elif choice=="transaction":
        try:

            cursor.execute("select * from transaction")
            i=cursor.fetchall()
            for i in i:
                print(i)

        except:
             print("NO Transaction Viewed")
             


    elif choice=="order details":

        try:

            cursor.execute("select * from order_details")
            i=cursor.fetchall()
            for i in i:
                print(i)

        except:
             print("NO Order Details Viewed")
             


    elif choice=="customer":
        try:

            cursor.execute("select * from customer")
            i=cursor.fetchall()
            for i in i:
                print(i)

        except:
             print("NO Customer Details Viewed")
             

    else:
        print("Invalid choice! Try again.")

        
  
cursor.close()
conn.close()
