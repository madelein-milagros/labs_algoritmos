from collections import deque

class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.completion_time = 0

def round_robin_scheduler(processes, quantum):
    queue = deque(processes)  # Cola circular
    time = 0  # Tiempo global

    while queue:
        process = queue.popleft()

        if process.remaining_time > quantum:
            time += quantum
            process.remaining_time -= quantum
            queue.append(process)  # Reagendar proceso
        else:
            time += process.remaining_time
            process.remaining_time = 0
            process.completion_time = time
            process.turnaround_time = process.completion_time
            process.waiting_time = process.turnaround_time - process.burst_time

    # Mostrar métricas
    print(f"{'Proceso':<10}{'BT':<10}{'WT':<10}{'TAT':<10}")
    total_wt = total_tat = 0
    for p in processes:
        print(f"{p.pid:<10}{p.burst_time:<10}{p.waiting_time:<10}{p.turnaround_time:<10}")
        total_wt += p.waiting_time
        total_tat += p.turnaround_time

    n = len(processes)
    print(f"\nTiempo promedio de espera: {total_wt / n:.2f}")
    print(f"Tiempo promedio de retorno: {total_tat / n:.2f}")

# 🔧 Ejemplo de uso
procesos = [
    Process('P1', 10),
    Process('P2', 5),
    Process('P3', 8)
]

quantum = 4
round_robin_scheduler(procesos, quantum)
