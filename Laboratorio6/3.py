#3
import random
from collections import deque

class Vehicle:
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time

class TrafficSimulation:
    def __init__(self, duration, green_light_duration):
        self.time = 0
        self.duration = duration
        self.green_light_duration = green_light_duration
        self.queues = {
            "NS": deque(),  # North-South
            "EW": deque()   # East-West
        }
        self.stats = {
            "total_wait_time": 0,
            "vehicles_passed": 0,
            "max_queue_lengths": {
                "NS": 0,
                "EW": 0
            }
        }

    def run(self):
        while self.time < self.duration:
            direction = "NS" if (self.time // self.green_light_duration) % 2 == 0 else "EW"

            # Random vehicle arrivals
            if random.random() < 0.5:  # 50% chance a vehicle arrives for NS
                self.queues["NS"].append(Vehicle(self.time))
            if random.random() < 0.5:  # 50% chance a vehicle arrives for EW
                self.queues["EW"].append(Vehicle(self.time))

            # Update max queue lengths
            for dir in self.queues:
                self.stats["max_queue_lengths"][dir] = max(
                    self.stats["max_queue_lengths"][dir],
                    len(self.queues[dir])
                )

            # Let up to 1 vehicle pass per second during green light
            if self.queues[direction]:
                vehicle = self.queues[direction].popleft()
                wait_time = self.time - vehicle.arrival_time
                self.stats["total_wait_time"] += wait_time
                self.stats["vehicles_passed"] += 1

            self.time += 1

        self.report()

    def report(self):
        print("\n--- Simulation Report ---")
        print(f"Total vehicles passed: {self.stats['vehicles_passed']}")
        if self.stats['vehicles_passed'] > 0:
            avg_wait = self.stats["total_wait_time"] / self.stats["vehicles_passed"]
        else:
            avg_wait = 0
        print(f"Average wait time: {avg_wait:.2f} seconds")
        print("Max queue lengths:")
        for dir, length in self.stats["max_queue_lengths"].items():
            print(f"  {dir}: {length}")

# Run the simulation
sim = TrafficSimulation(duration=60, green_light_duration=10)
sim.run()
