import redis

def test_redis_connection():
    try:
        # Connect to Redis container
        r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

        # Test: Set a key
        r.set("flight:test", "Redis is working!")

        # Test: Retrieve the key
        value = r.get("flight:test")
        print("✅ Redis connection successful.")
        print("🔁 Test Key Retrieved:", value)
    except redis.exceptions.ConnectionError as e:
        print("❌ Redis connection failed:", e)

if __name__ == "__main__":
    test_redis_connection()
