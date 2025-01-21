import schedule
import time

def rotina(tarefa, intervalo):
    schedule.every(intervalo).minutes.do(tarefa)

    print(f"Executando a tarefa a cada {intervalo} minuto(s)...")

    while True:
        schedule.run_pending()
        time.sleep(1)