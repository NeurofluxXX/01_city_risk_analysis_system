import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="geo_ai_learning",
        user="postgres",
        password="12345",
        port="5432"
    )
    return conn