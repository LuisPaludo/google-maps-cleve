from datetime import datetime

def detect_jam(speed_reading_intervals, distance, city_origin, city_destination):
    jams = []
    for item in speed_reading_intervals:
        if item.speed == 'TRAFFIC_JAM':
            jams.append(item)
            detect_proximity(item, speed_reading_intervals, distance, city_origin, city_destination)
    return jams

def detect_proximity(item, speed_reading_intervals, distance, city_origin, city_destination):
    last_point = speed_reading_intervals[-1].end_polyline_point_index

    initial_km = round(item.start_polyline_point_index*distance/last_point, 2)
    final_km = round(item.end_polyline_point_index*distance/last_point, 2)
    current_time = datetime.now().strftime("%H:%M:%S")
        
    print(f"[{current_time}] Engarrafamento detectado: {initial_km}Km até {final_km}Km") 

    return initial_km, final_km, current_time
     