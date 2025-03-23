import mysql.connector

def book_flight(flight_id):
    cnx = mysql.connector.connect(
        user='root',
        password='New123',
        host='127.0.0.1',
        database='flight_reservation'
    )
    cursor = cnx.cursor()

    # Check seat availability
    cursor.execute("SELECT Seat_Availability FROM flights WHERE Flight_ID = %s", (flight_id,))
    result = cursor.fetchone()

    if not result:
        print("🚫 Flight not found.")
    elif result[0] <= 0:
        print("❌ Sorry, no seats available.")
    else:
        # Book the flight (reduce availability)
        cursor.execute("UPDATE flights SET Seat_Availability = Seat_Availability - 1 WHERE Flight_ID = %s", (flight_id,))
        cnx.commit()
        print("✅ Flight booked successfully!")

    cursor.close()
    cnx.close()

# Get user input
flight_id = input("Enter the Flight ID you want to book: ")
if flight_id.isdigit():
    book_flight(int(flight_id))
else:
    print("❗ Invalid Flight ID.")
