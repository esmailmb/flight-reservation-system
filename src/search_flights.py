import mysql.connector

# Function to search flights
def search_flights(departure, arrival, date, seat_class, max_price):
    cnx = mysql.connector.connect(
        user='root',
        password='New123',
        host='127.0.0.1',
        database='flight_reservation'
    )
    cursor = cnx.cursor()

    query = """
    SELECT Flight_ID, Airline, Departure_City, Arrival_City, Departure_Time, Arrival_Time, Seat_Class, Price
    FROM flights
    WHERE Departure_City = %s 
      AND Arrival_City = %s 
      AND Departure_Time LIKE %s
      AND Seat_Class = %s
      AND Price <= %s
    """
    cursor.execute(query, (departure, arrival, f"{date}%", seat_class, max_price))

    flights = cursor.fetchall()
    cursor.close()
    cnx.close()

    return flights

# Run search
departure = input("Enter Departure City: ")
arrival = input("Enter Arrival City: ")
date = input("Enter Date (YYYY-MM-DD): ")
seat_class = input("Enter Seat Class (Economy, Business, First): ")
max_price = float(input("Enter Max Price: "))

results = search_flights(departure, arrival, date, seat_class, max_price)

# Display results
if results:
    print("\n✈️ Available Flights:")
    for flight in results:
        print(f"Flight {flight[0]} | {flight[1]} | {flight[2]} -> {flight[3]} | {flight[4]} - {flight[5]} | {flight[6]} | ${flight[7]}")
else:
    print("\n🚫 No flights found for the given criteria.")
