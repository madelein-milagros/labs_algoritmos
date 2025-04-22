from collections import deque
import random

class Customer:
    def __init__(self, customer_id, item_count, arrival_time):
        self.id = customer_id
        self.items = item_count
        self.arrival_time = arrival_time
        self.remaining_items = item_count
        self.start_time = None
        self.end_time = None

class CheckoutLane:
    def __init__(self, lane_id, processing_rate):
        self.lane_id = lane_id
        self.processing_rate = processing_rate
        self.queue = deque()
        self.current_customer = None

    def add_customer(self, customer, current_time):
        self.queue.append(customer)

    def process(self, current_time):
        if not self.current_customer and self.queue:
            self.current_customer = self.queue.popleft()
            self.current_customer.start_time = current_time

        if self.current_customer:
            self.current_customer.remaining_items -= self.processing_rate
            if self.current_customer.remaining_items <= 0:
                self.current_customer.end_time = current_time
                finished = self.current_customer
                self.current_customer = None
                return finished
        return None

class Supermarket:
    def __init__(self, lanes):
        self.lanes = lanes
        self.time = 0
        self.finished_customers = []

    def find_shortest_lane(self):
        return min(self.lanes, key=lambda lane: len(lane.queue) + (1 if lane.current_customer else 0))

    def add_customer(self, customer):
        lane = self.find_shortest_lane()
        lane.add_customer(customer, self.time)

    def simulate(self, total_time, new_customer_probability=0.3):
        customer_id_counter = 1

        for t in range(total_time):
            self.time = t

            # Simulate the arrival of new customers
            if random.random() < new_customer_probability:
                items = random.randint(5, 20)
                customer = Customer(customer_id_counter, items, t)
                self.add_customer(customer)
                customer_id_counter += 1

            # Process each checkout lane
            for lane in self.lanes:
                finished = lane.process(t)
                if finished:
                    self.finished_customers.append(finished)

        # Calculate statistics
        wait_times = [c.start_time - c.arrival_time for c in self.finished_customers]
        total_times = [c.end_time - c.arrival_time for c in self.finished_customers]
        avg_wait = sum(wait_times) / len(wait_times) if wait_times else 0
        avg_total = sum(total_times) / len(total_times) if total_times else 0

        print(f"\n Simulation completed ({total_time} time units)")
        print(f" Customers served: {len(self.finished_customers)}")
        print(f" Average wait time: {avg_wait:.2f}")
        print(f" Average total time per customer: {avg_total:.2f}")

# Run simulation
if __name__ == "__main__":
    # Create 3 lanes with different speeds (items per time unit)
    lanes = [
        CheckoutLane(lane_id=1, processing_rate=1),
        CheckoutLane(lane_id=2, processing_rate=2),
        CheckoutLane(lane_id=3, processing_rate=3),
    ]

    market = Supermarket(lanes)
    market.simulate(total_time=100)
