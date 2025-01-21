import psycopg2
from decouple import config
from datetime import date

def start_db():
    try:
        conn = psycopg2.connect(
            f"dbname={config('DB_NAME')} user={config('POSTGRES_USER')} password={config('POSTGRES_PASSWORD')}"
            )
        cur = conn.cursor()

        create_table_sql = """
        CREATE TABLE IF NOT EXISTS data (
            pk SERIAL PRIMARY KEY,
            initial_km FLOAT,
            final_km FLOAT,
            time DATE,
            city_origin VARCHAR(255),
            city_destination VARCHAR(255),
            city_closed VARCHAR(255),
            encoded_polyline TEXT,
            avg_time_closed DATE
        );
        """
        cur.execute(create_table_sql)
        
        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error creating table: {e}")


def connect():
    conn = psycopg2.connect(
            f"dbname={config('DB_NAME')} user={config('POSTGRES_USER')} password={config('POSTGRES_PASSWORD')}"
        )
    cur = conn.cursor()
    return conn, cur


def save_data(
        initial_km:float, 
        final_km:float,
        time:date,
        city_origin:str,
        city_destination:str,
        city_closed:str,
        encoded_polyline:str,
        avg_time_closed:date,
        ):
    try:
        conn, cur = connect()
        data_to_insert = (
            initial_km,
            final_km,
            time,
            city_origin,
            city_closed,
            city_destination,
            encoded_polyline,
            avg_time_closed
        )

        insert_sql = """
        INSERT INTO data (initial_km, final_km, time, city_origin, city_closed, city_destination, encoded_polyline, avg_time_closed)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """

        cur.execute(insert_sql, data_to_insert)
        print("Data saved with success.")
        conn.commit()
        cur.close()
        conn.close()
        

    except Exception as e:
        print(f"Error saving data: {e}")

def get_last_three_times():
    try:
        conn, cur = connect()
        select_sql = """
        SELECT 
        time 
        FROM data
        ORDER BY time DESC
        LIMIT 3
        ;
        """
        cur.execute(select_sql)
        return cur.fetchall()

    except Exception as e:
        print(f"Error saving data: {e}")