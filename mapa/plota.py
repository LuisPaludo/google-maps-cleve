import googlemaps
import matplotlib.pyplot as plt
from decouple import config

def plota_mapa(encoded_polyline, speedReadingIntervals):
    gmaps = googlemaps.Client(key=config('GOOGLE_API_KEY')) 
    decoded_path = googlemaps.convert.decode_polyline(encoded_polyline)

    speed_colors = {
        'NORMAL': 'green',
        'SLOW': 'yellow',
        'TRAFFIC_JAM': 'red'
    }

    plt.figure(figsize=(10, 6))
    for interval in speedReadingIntervals:
        start_idx = interval['startPolylinePointIndex']
        end_idx = interval['endPolylinePointIndex']
        color = speed_colors[interval['speed']]
        
        segment = decoded_path[start_idx:end_idx + 1]
        latitudes = [point['lat'] for point in segment]
        longitudes = [point['lng'] for point in segment]
        
        plt.plot(longitudes, latitudes, color=color, linewidth=2, label=interval['speed'] if color not in plt.gca().get_legend_handles_labels()[1] else "")

    plt.title("Rota com Condições de Tráfego")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend(title="Condição de Tráfego")
    plt.grid(True)
    plt.show()


