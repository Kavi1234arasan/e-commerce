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
               CREATE TABLE IF NOT EXISTS transaction(
               ID INT PRIMARY KEY AUTO_INCREMENT,
               Customer_ID INT,
               Payment_Method VARCHAR(100),
               Total_Amount FLOAT,
               Status VARCHAR(100),
               Payment_Date DATE,
               Payment_Time TIME,

                FOREIGN KEY (Customer_ID) REFERENCES customer(Customer_ID)

               
               
      )
""")




def payment_method(Customer_ID, Payment_Method, Total_Amount, Status, Payment_Date, Payment_Time):

    query="INSERT INTO transaction(Customer_ID, Payment_Method,Total_Amount,Status ,Payment_Date,Payment_Time) values(%s,%s,%s,%s,%s,%s)"
    values=(Customer_ID, Payment_Method,Total_Amount,Status ,Payment_Date,Payment_Time)
    cursor.execute(query,values)
    conn.commit()



while True:
    try:
        Customer_ID = int(input("Enter your Customer ID: "))
        cursor.execute("SELECT * FROM customer WHERE Customer_ID = %s", (Customer_ID,))

        rows=cursor.fetchall()
        for i in rows:
            print("customer details:",i)
            continue
    
        print("\nChoose your Payment Method:")
        print("1: G Pay")
        print("2: Phone Pay")
        print("3: Amazon Pay")
        print("4: Pay Pal")
        print("5: Cash on Delivery")

        option = input("Enter option number (1-5): ")
        payment_methods = {
            '1': 'G Pay',
            '2': 'Phone Pay',
            '3': 'Amazon Pay',
            '4': 'Pay Pal',
            '5': 'Cash on Delivery'
        }

        if option not in payment_methods:
            print("Invalid payment method.")
            continue

        Payment_Method = payment_methods[option]
        print("You selected:", Payment_Method)

        

        Total_Amount = input("Enter your total amount: ")
        Total_Amount = float(Total_Amount)

        

        confirm = input("Please click 'yes' to Pay or 'no' to cancel: ").lower()
        if confirm != 'yes':
            print("Payment canceled.")
            continue
        print("Processing your payment...")
        Status = 'Paid'
        
        now = datetime.now()
        Payment_Date = now.date()
        Payment_Time = now.time()

        
        payment_method(Customer_ID, Payment_Method, Total_Amount, Status, Payment_Date, Payment_Time)

        print("Payment successful! Thank You.\n")

    except:
        print("Error occurred:")
        continue


    

cursor.close()
conn.close()
