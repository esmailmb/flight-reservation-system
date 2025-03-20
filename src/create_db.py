import mysql.connector

# Connect to MySQL
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="New123",
    port=3300
)
cursor = cnx.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS flight_reservation")
cursor.execute("USE flight_reservation")

# Create flights table
query = """
CREATE TABLE IF NOT EXISTS flights (
    Flight_ID INT PRIMARY KEY,
    Airline VARCHAR(50),
    Departure_City VARCHAR(50),
    Arrival_City VARCHAR(50),
    Departure_Time VARCHAR(20),
    Arrival_Time VARCHAR(20),
    Flight_Type VARCHAR(20),
    Aircraft_Type VARCHAR(50),
    Seats_Available INT,
    Price DECIMAL(10,2),
    Meal_Option VARCHAR(20),
    Flight_Status VARCHAR(20),
    Gate_Number INT,
    Gate_Type VARCHAR(20),
    Duration_Hours DECIMAL(4,2),
    Baggage_Allowance VARCHAR(20),
    Cancellation_Policy VARCHAR(50),
    Seat_Class VARCHAR(20),
    WiFi_Available VARCHAR(10),
    Entertainment_Options VARCHAR(50),
    Loyalty_Points_Earned INT,
    Layovers VARCHAR(20),
    Boarding_Group VARCHAR(10),
    Eco_Friendly_Flight VARCHAR(10),
    Crew_Language_Support VARCHAR(50),
    Inflight_Services VARCHAR(50),
    Seat_Availability VARCHAR(30),
    Ticket_Flexibility VARCHAR(50),
    Discounts_Available VARCHAR(50),
    Customer_Rating DECIMAL(3,1)
);
"""
cursor.execute(query)

print("✅ Database and tables created successfully!")

# Close connection
cnx.commit()
cursor.close()
cnx.close()
