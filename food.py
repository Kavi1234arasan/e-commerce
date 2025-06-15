

import pymysql.cursors

conn=pymysql.connect(
    host="localhost",
    user="root",
    password="kavi8248",
    database="shopping"
    
)

cursor=conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS food(
               ID INT PRIMARY KEY AUTO_INCREMENT,
               Dish_Name varchar(100),
               Price float,
               Restaurant_Name varchar(100),
               Ratings float
    )
""")


def add_dish(ID,Dish_Name,Restaurant_Name,Ratings,Price):
    query="INSERT INTO food(ID,Dish_Name,Restaurant_Name,Ratings,Price) values(%s,%s,%s,%s,%s)"
    values=(ID,Dish_Name,Restaurant_Name,Ratings,Price)
    cursor.execute(query,values)
    conn.commit()
    print("Add successfully")


def view_dish():
    cursor.execute("SELECT * FROM food")
    dishes=cursor.fetchall()
    for dish in dishes:
        print(dish)

def update_dish():
    query="UPDATE food SET Dish_Name=%s,Restaurant_Name=%s,Ratings%s,Price=%s WHERE ID=%s"
    values=(ID,Dish_Name,Restaurant_Name,Ratings,Price)
    cursor.execute(query,values)
    conn.commit()
    print("update successfully")

def delete_dish():
    query = "DELETE FROM food WHERE id = %s"
    values=("ID")
    cursor.execute(query,values)
    conn.commit()
    print("User deleted successfully!")


while True:

    choice=input("Enter your choice (add/view/update/delete) in lower case:")

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
            break

    else:
        print("Invalid choice! Try again.")
            
     
cursor.close()
conn.close()














