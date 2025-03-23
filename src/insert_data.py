import mysql.connector
import csv

# Establishing database connection
cnx = mysql.connector.connect(
    user='root',
    password='New123',
    host='127.0.0.1',
    database='flight_reservation'
)
cursor = cnx.cursor()

# SQL query to insert data
query = """
INSERT INTO flights (
    Airline, Flight_Number, Departure_City, Arrival_City, 
    Departure_Date, Arrival_Date, Departure_Time, Arrival_Time, 
    Price, Duration_Hours, Baggage_Allowance, Seat_Class, 
    WiFi_Available, Entertainment_Options, Loyalty_Points_Earned, 
    Boarding_Group, Eco_Friendly_Flight, Crew_Language_Support, 
    Seat_Availability, Ticket_Flexibility, Discounts_Available, Customer_Rating
) 
VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)
"""

# Reading data from CSV
# Reading data from CSV
with open('data/flights_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row

    for row in reader:
        # Convert 'Yes'/'No' to 1/0 for specific boolean columns
        row[12] = 1 if row[12].strip().lower() == 'yes' else 0  # WiFi_Available
        row[13] = 1 if row[13].strip().lower() == 'yes' else 0  # Entertainment_Options
        row[16] = 1 if row[16].strip().lower() == 'yes' else 0  # Eco_Friendly_Flight
        row[20] = 1 if row[20].strip().lower() == 'yes' else 0  # Discounts_Available

        # Insert into DB
        cursor.execute(query, row)


# Committing changes
cnx.commit()
