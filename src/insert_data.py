import mysql.connector
import csv

# Connect to MySQL database
cnx = mysql.connector.connect(
    user='root',
    password='New123',
    host='127.0.0.1',
    database='flight_reservation'
)
cursor = cnx.cursor()

# SQL Query for inserting data
query = """
INSERT INTO flights (
    Flight_ID, Airline, Departure_City, Arrival_City, Departure_Time, Arrival_Time,
    Flight_Type, Aircraft_Type, Seats_Available, Price, Meal_Option, Flight_Status,
    Gate_Number, Gate_Type, Duration_Hours, Baggage_Allowance, Cancellation_Policy,
    Seat_Class, WiFi_Available, Entertainment_Options, Loyalty_Points_Earned, Layovers,
    Boarding_Group, Eco_Friendly_Flight, Crew_Language_Support, Inflight_Services,
    Seat_Availability, Ticket_Flexibility, Discounts_Available, Customer_Rating
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)
"""

# Read data from CSV file and insert into database
with open('data/flights_data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        cursor.execute(query, row)

# Commit changes
cnx.commit()

# Close connection
cursor.close()
cnx.close()

print("✅ Flight data inserted successfully!")
