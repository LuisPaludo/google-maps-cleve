from map import map, map_analysis, plot, speed_reading_interval as sri
from main_schedule import schedule_by_interval
from connect_db import connection

city_origin = "Clevelândia, PR, Brasil"
city_destination = "Pato Branco, PR, Brasil"

def main():
    encoded_polyline, jam_info, distance = map.retrieve_info(
        city_origin=city_origin, 
        city_destination=city_destination
        )
    
    jam_info = sri.parse_speed_reading_intervals(jam_info)

    map_analysis.detect_jam(
        speed_reading_intervals=jam_info, 
        distance=distance, 
        city_origin=city_origin, city_destination=city_destination,
        encoded_polyline=encoded_polyline
        )
    
    connection.connect()

if __name__ == "__main__":
    intervalo = 15
    connection.start_db()
    main()
    schedule_by_interval(main, intervalo)

