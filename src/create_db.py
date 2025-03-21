import mysql.connector

# Connect to MySQL server
cnx = mysql.connector.connect(
    user='root',
    password='New123',
    host='127.0.0.1'
)
cursor = cnx.cursor()

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS flight_reservation")
cursor.execute("USE flight_reservation")

# Create Flights Table with Updated Attributes
query = """
CREATE TABLE IF NOT EXISTS flights (
    Flight_ID INT PRIMARY KEY AUTO_INCREMENT,
    Airline VARCHAR(50),
    Departure_City VARCHAR(50),
    Arrival_City VARCHAR(50),
    Departure_Time DATETIME,
    Arrival_Time DATETIME,
    Price DECIMAL(10,2),
    Duration_Hours DECIMAL(5,2),
    Baggage_Allowance VARCHAR(50),
    Seat_Class VARCHAR(20),
    WiFi_Available BOOLEAN,
    Entertainment_Options BOOLEAN,
    Loyalty_Points_Earned INT,
    Boarding_Group VARCHAR(10),
    Eco_Friendly_Flight BOOLEAN,
    Crew_Language_Support VARCHAR(100),
    Seat_Availability INT,
    Ticket_Flexibility VARCHAR(50),
    Discounts_Available BOOLEAN,
    Customer_Rating DECIMAL(3,1)
);
"""
cursor.execute(query)

print("✅ Database and tables created successfully!")

# Close connection
cnx.commit()
cursor.close()
cnx.close()
