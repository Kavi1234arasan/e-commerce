
import pymysql.cursors

conn=pymysql.connect(
    host="localhost",
    user="root",
    password="kavi8248",
    database="shopping",
     cursorclass=pymysql.cursors.DictCursor
    
)

cursor=conn.cursor()



cursor.execute("""
               CREATE TABLE IF NOT EXISTS customer(
               Customer_ID int primary key AUTO_INCREMENT,
               Customer_Name varchar(100) NOT NULL,
               Email varchar(255),
               Contact BIGINT,
               Address varchar(255)
    )
""")



def customer_login(Customer_Name,Email,Contact,Address):
     
        query="INSERT INTO customer(Customer_Name,Email,Contact,Address) values(%s,%s,%s,%s)"
        values=(Customer_Name,Email,Contact,Address)
        cursor.execute(query,values)
        conn.commit()
        
        print("Login successful. Welcome,",Customer_Name)



while True:

    Login=input("Please Login This Page (type=login or exit):")

    if Login=="login":
        try:

             User_Name = input("Enter Your Name:")
             Email = input("Enter Your Email:")
             Contact = int(input("Enter Your Contact Number:"))
             Address = input("Enter Your Current Address:")

             customer_login(User_Name,Email,Contact,Address)

            

        except:
                print("Login Failed! Please Try again.")
                




    elif Login == "exit":
            print("Exiting...")
            break
            

    else:
        print("Please Try again!")
        




cursor.close()
conn.close()
