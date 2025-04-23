import queue

class Customer:
    def __init__(self, customer_id, item_count, arrival_time):
        self.customer_id = customer_id
        self.item_count = item_count
        self.arrival_time = arrival_time
        self.remaining_items = item_count
        self.start_time = None
        self.end_time = None
class CheckoutLane:
    def __init__(self, lane_id, processing_rate):
        self.lane_id = lane_id
        self.processing_rate = processing_rate  
        self.queue = queue.Queue()
        self.current_customer = None

    def add_customer(self, customer):
        self.queue.put(customer)

    def process(self, current_time):
        # If no one is being processed, take the next customer
        if self.current_customer is None and not self.queue.empty():
            self.current_customer = self.queue.get()
            self.current_customer.start_time = current_time

        if self.current_customer:
            self.current_customer.remaining_items -= self.processing_rate
            if self.current_customer.remaining_items <= 0:
                self.current_customer.end_time = current_time
                finished_customer = self.current_customer
                self.current_customer = None
                return finished_customer
        return None
class Supermarket:
    def __init__(self, num_lanes, processing_rates):
        self.time = 0
        self.lanes = [CheckoutLane(i, rate) for i, rate in enumerate(processing_rates)]
        self.all_customers = []
        self.completed_customers = []

    def add_customer(self, customer):
        # Choose the lane with the shortest queue
        shortest_lane = min(self.lanes, key=lambda lane: lane.queue.qsize())
        shortest_lane.add_customer(customer)
        self.all_customers.append(customer)

    def simulate(self, total_time, arriving_customers):
        for t in range(total_time):
            self.time = t

            # Add new customers arriving at this time
            for customer in arriving_customers.get(t, []):
                self.add_customer(customer)

            # Process customers in each lane
            for lane in self.lanes:
                finished = lane.process(t)
                if finished:
                    self.completed_customers.append(finished)

    def get_statistics(self):
        wait_times = [
            cust.end_time - cust.arrival_time
            for cust in self.completed_customers
        ]
        average_wait = sum(wait_times) / len(wait_times) if wait_times else 0
        throughput = len(self.completed_customers)

        return {
            "average_wait_time": average_wait,
            "total_customers_processed": throughput
        }

# Customers arriving at each time step
arrivals = {
    0: [Customer(1, 5, 0), Customer(2, 8, 0)],
    1: [Customer(3, 3, 1)],
    3: [Customer(4, 6, 3)],
    5: [Customer(5, 7, 5)]
}

market = Supermarket(num_lanes=2, processing_rates=[2, 3])  
market.simulate(total_time=15, arriving_customers=arrivals)

# Print statistics
stats = market.get_statistics()
print("Average Wait Time:", stats["average_wait_time"])
print("Total Customers Processed:", stats["total_customers_processed"])
