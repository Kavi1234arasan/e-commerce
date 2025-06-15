

import pymysql.cursors
from datetime import datetime

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="kavi8248",
    database="shopping"
)

cursor = conn.cursor()



cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_details (
        Order_ID INT PRIMARY KEY AUTO_INCREMENT,
        Order_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        Customer_ID INT,
        ID INT,
        Dish_Name VARCHAR(100),
        Quantity INT,
        Total_Price Float,
        
        FOREIGN KEY (Customer_ID) REFERENCES customer(Customer_ID),
        FOREIGN KEY (ID) REFERENCES food(ID)
        
    )
""")



def details(Order_Date,Customer_ID, ID,Dish_Name,Quantity ,Total_Price ):

        query="INSERT INTO order_details(Order_Date,Customer_ID, ID,Dish_Name,Quantity ,Total_Price) values(%s,%s,%s,%s,%s,%s)"
        values=(Order_Date, Customer_ID, ID, Dish_Name, Quantity, Total_Price)
        cursor.execute(query,values)
        conn.commit()

while True:

        try:
                order_date = datetime.now()

                
                Customer_ID = int(input("Enter your Customer ID: "))
                cursor.execute("SELECT * FROM customer WHERE Customer_ID = %s", (Customer_ID,))

                rows=cursor.fetchall()
                for i in rows:
                        print("customer details:",i)
                        continue


                ID = int(input("Enter Dish ID: "))
                cursor.execute("SELECT Dish_Name FROM food WHERE ID = %s", (ID,))
                result = cursor.fetchone()

                for j in result:
                        print("food details is:",j)
                        continue

                Dish_Name = j
                
                cursor.execute("SELECT Price FROM food WHERE ID = %s", (ID,))
                result = cursor.fetchone()
                for j in result:
                        print("food price is:",j)
                        continue

                Price = j

        
                
                Quantity = int(input("Enter quantity: "))

                Total_Price = Quantity*j
                print("Total Amount :",Total_Price)
                
                
                details(order_date, Customer_ID, ID, Dish_Name, Quantity, Total_Price)

                
                print("Order placed successfully!")

        except:
                print("Order failed:")


        return_order = input("Do you want to place another order? (yes/no): ")
        if return_order != 'yes':
                break



cursor.close()
conn.close()

