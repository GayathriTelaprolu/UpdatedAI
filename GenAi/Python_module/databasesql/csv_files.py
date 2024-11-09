import pandas as pd
import mysql.connector

# Function to connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1', 
             port='3307', # Use the IP or hostname of your MySQL server
            user='myuser',     # Your MySQL username
            password='mypassword',  # Your MySQL password
            database='mydatabase'  # The database where tables exist
        )
        if connection.is_connected():
            print("Connected to the database")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to insert data into a table
def insert_data_from_csv(connection, csv_file, insert_query):
    cursor = connection.cursor()
    try:
        # Load CSV data
        data = pd.read_csv(csv_file)
        # Iterate through each row in the DataFrame and insert into table
        for index, row in data.iterrows():
            cursor.execute(insert_query, tuple(row))
        connection.commit()
        print(f"Data from {csv_file} inserted successfully.")
    except Exception as e:
        print(f"Error while inserting data: {e}")
    finally:
        cursor.close()

def main():
    connection = connect_to_database()
    if connection is None:
        return
    
    # Insert data into 'Orders' table
    orders_insert_query = """
    INSERT INTO Orders (order_id, customer_id, order_date, total_amount, shipping_address)
    VALUES (%s, %s, %s, %s, %s)
    """
    insert_data_from_csv(connection, 'orders.csv', orders_insert_query)

    # Insert data into 'Order_Items' table
    order_items_insert_query = """
    INSERT INTO OrderItems (order_item_id, order_id, product_id, quantity, price)
    VALUES (%s, %s, %s, %s, %s)
    """
    insert_data_from_csv(connection, 'order_items.csv', order_items_insert_query)

    # Insert data into 'Payments' table
    payments_insert_query = """
    INSERT INTO Payments (payment_id, order_id, payment_date, amount, payment_method)
    VALUES (%s, %s, %s, %s, %s)
    """
    insert_data_from_csv(connection, 'payments.csv', payments_insert_query)

    # Insert data into 'Shipping_Details' table
    shipping_details_insert_query = """
    INSERT INTO Shipping (shipping_id, order_id, shipping_date, carrier, tracking_number)
    VALUES (%s, %s, %s, %s, %s)
    """
    insert_data_from_csv(connection, 'shipping_details.csv', shipping_details_insert_query)

    connection.close()

if __name__ == "__main__":
    main()
