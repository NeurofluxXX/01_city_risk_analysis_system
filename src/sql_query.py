import pandas as pd
from database import get_connection

def load_city_risk_data():
    conn = get_connection()

    sql = """
    SELECT r.city, r.risk, p.population
    FROM city_risk AS r
        INNER JOIN city_population AS p 
        ON r.city = p.city;
    """

    data = pd.read_sql(sql, conn)

    conn.close()

    return data

