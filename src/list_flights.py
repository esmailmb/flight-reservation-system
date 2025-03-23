import mysql.connector

# Connect to MySQL
cnx = mysql.connector.connect(
    user='root',
    password='New123',
    host='127.0.0.1',
    database='flight_reservation'
)

cursor = cnx.cursor()
cursor.execute("""
    SELECT Flight_ID, Airline, Departure_City, Arrival_City, Departure_Time, Seat_Class, Price 
    FROM flights
    LIMIT 50
""")
flights = cursor.fetchall()

print("📋 Flights in Database:")
for f in flights:
    print(f"Flight {f[0]} | {f[1]} | {f[2]} → {f[3]} | {f[4]} | {f[5]} | ${f[6]}")

cursor.close()
cnx.close()
