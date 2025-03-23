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

# Build a unique cache key
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

    # 2. If not in cache, query MySQL
    cnx = get_mysql_connection()
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

    # 3. Store result in Redis cache for 10 minutes
    cache.setex(key, 600, json.dumps(flights))  # 600 seconds = 10 minutes

    cursor.close()
    cnx.close()
    return flights

# CLI interaction
departure = input("Enter Departure City: ")
arrival = input("Enter Arrival City: ")
date = input("Enter Date (YYYY-MM-DD): ")
seat_class = input("Enter Seat Class (Economy, Business, First): ")
max_price = float(input("Enter Max Price: "))

results = search_flights(departure, arrival, date, seat_class, max_price)

if results:
    print("\n✈️ Available Flights:")
    for flight in results:
        print(f"Flight {flight[0]} | {flight[1]} | {flight[2]} -> {flight[3]} | {flight[4]} - {flight[5]} | {flight[6]} | ${flight[7]}")
else:
    print("\n🚫 No flights found for the given criteria.")
