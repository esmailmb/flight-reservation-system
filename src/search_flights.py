import mysql.connector
import redis
import json

# Connect to Redis
cache = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

# Connect to MySQL
def get_mysql_connection():
    return mysql.connector.connect(
        user='root',
        password='New123',
        host='127.0.0.1',
        database='flight_reservation'
    )

# Build a unique cache key for each search
def build_cache_key(departure, arrival, date, seat_class, max_price):
    return f"{departure}:{arrival}:{date}:{seat_class}:{max_price}"

# Search flights
def search_flights(departure, arrival, date, seat_class, max_price):
    key = build_cache_key(departure, arrival, date, seat_class, max_price)

    # 1. Try Redis cache
    cached = cache.get(key)
    if cached:
        print("⚡ Result from Redis Cache:")
        return json.loads(cached)

    # 2. If not cached, query MySQL
    cnx = get_mysql_connection()
    cursor = cnx.cursor()

    query = """
    SELECT Flight_ID, Airline, Departure_City, Arrival_City, Departure_Time, Arrival_Time, Seat_Class, Price
    FROM flights
    WHERE Departure_City LIKE %s 
      AND Arrival_City LIKE %s 
      AND Departure_Time LIKE %s
      AND Seat_Class = %s
      AND Price <= %s
    """

    cursor.execute(query, (f"%{departure}%", f"%{arrival}%", f"{date}%", seat_class, max_price))
    flights = cursor.fetchall()

    # Convert datetime objects to strings for JSON
    flights_serializable = []
    for f in flights:
        flights_serializable.append([
            f[0],  # Flight_ID
            f[1],  # Airline
            f[2],  # Departure_City
            f[3],  # Arrival_City
            str(f[4]),  # Departure_Time
            str(f[5]),  # Arrival_Time
            f[6],  # Seat_Class
            float(f[7])  # Price
        ])

    # Cache for 10 minutes
    cache.setex(key, 600, json.dumps(flights_serializable))

    cursor.close()
    cnx.close()
    return flights_serializable

# ------------------------ CLI Interface ------------------------

departure = input("Enter Departure City: ").strip()
arrival = input("Enter Arrival City: ").strip()
date = input("Enter Date (YYYY-MM-DD): ").strip()
seat_class = input("Enter Seat Class (Economy, Business, First): ").strip()
max_price = float(input("Enter Max Price: ").strip())

results = search_flights(departure, arrival, date, seat_class, max_price)

if results:
    print("\n✈️ Available Flights:")
    for flight in results:
        print(f"Flight {flight[0]} | {flight[1]} | {flight[2]} → {flight[3]} | {flight[4]} - {flight[5]} | {flight[6]} | ${flight[7]}")
else:
    print("\n🚫 No flights found for the given criteria.")

