import schedule
import time

def schedule_by_interval(task, interval):
    schedule.every(interval).minutes.do(task)

    print(f"Executando a tarefa a cada {interval} minuto(s)...")

    while True:
        schedule.run_pending()
        time.sleep(1)