from datetime import datetime
from connect_db import connection

def detect_jam(speed_reading_intervals, distance, city_origin, city_destination, encoded_polyline):
    jams = []
    for item in speed_reading_intervals:
        if item.speed == 'TRAFFIC_JAM':
            jams.append(item)

    for jam in jams:
        detect_proximity(jam, speed_reading_intervals, distance)
        city_closed = get_city_closed(jams)
        avg_time_closed = get_avg_time_closed()
        save_jam(item, city_origin, city_destination, city_closed, encoded_polyline, avg_time_closed)
    

def detect_proximity(item, speed_reading_intervals, distance):
    last_point = speed_reading_intervals[-1].end_polyline_point_index

    item.initial_km = round(item.start_polyline_point_index*distance/last_point, 2)
    item.final_km = round(item.end_polyline_point_index*distance/last_point, 2)
    item.current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
    print(f"[{item.current_time}] Engarrafamento detectado: {item.initial_km}Km até {item.final_km}Km") 
    

def get_city_closed(jams):
    pass

def get_avg_time_closed():
    last_closed_times = connection.get_last_three_times()
    
    if not last_closed_times:
        return None
    


def save_jam(item, city_origin, city_destination, city_closed, encoded_polyline, avg_time_closed):
    connection.save_data(
        item.initial_km,
        item.final_km,
        item.current_time,
        city_origin,
        city_destination,
        city_closed,
        encoded_polyline,
        avg_time_closed
    )