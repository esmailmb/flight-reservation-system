import mysql.connector
import csv

# Connect to MySQL
cnx = mysql.connector.connect(
    user='root',
    password='New123',
    host='127.0.0.1',
    database='flight_reservation'
)
cursor = cnx.cursor()

# Open CSV File
with open('../data/flights_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row

    for row in reader:
        query = """
        INSERT INTO flights (
            Airline, Departure_City, Arrival_City, Departure_Time, Arrival_Time,
            Price, Duration_Hours, Baggage_Allowance, Seat_Class, WiFi_Available,
            Entertainment_Options, Loyalty_Points_Earned, Boarding_Group, Eco_Friendly_Flight,
            Crew_Language_Support, Seat_Availability, Ticket_Flexibility, Discounts_Available,
            Customer_Rating
        ) VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, 
            %s, %s, %s, %s, 
            %s
        )
        """
        cursor.execute(query, row)

# Commit and close
cnx.commit()
cursor.close()
cnx.close()

print("✅ Flight data inserted successfully!")
