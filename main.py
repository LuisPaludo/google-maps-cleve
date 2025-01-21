from mapa import mapa, plota, analisa_mapa, speed_reading_interval as sri
from rotina import rotina as rt

city_origin = "Clevelândia, PR, Brasil"
city_destination = "Pato Branco, PR, Brasil"

def tarefa():
    encoded_polyline, speedReadingIntervals, distance = mapa.busca_mapa(city_origin, city_destination)
    speedReadingIntervals = sri.parse_speed_reading_intervals(speedReadingIntervals)
    analisa_mapa.identifica_engarrafamento(speedReadingIntervals, distance, city_origin, city_destination)

if __name__ == "__main__":
    intervalo = 15
    tarefa()
    rt(tarefa, intervalo)

