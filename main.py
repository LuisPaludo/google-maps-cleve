from map import map, map_analysis, plot, speed_reading_interval as sri
from main_schedule import schedule_by_interval

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
        city_origin=city_origin, city_destination=city_destination
        )
    
    # plot.plot_map(
    #     encoded_polyline=encoded_polyline, 
    #     jam_info=jam_info
    #     )

if __name__ == "__main__":
    intervalo = 15
    main()
    schedule_by_interval(main, intervalo)

