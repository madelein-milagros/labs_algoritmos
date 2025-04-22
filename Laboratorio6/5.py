class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.start = 0  
        self.count = 0  

    def add(self, value):
        index = (self.start + self.count) % self.size
        if self.count < self.size:
            self.count += 1
        else:
            self.start = (self.start + 1) % self.size
        self.buffer[index] = value

    def get_latest(self):
        return [self.buffer[(self.start + i) % self.size] for i in range(self.count)]

    def get_stats(self):
        data = self.get_latest()
        if not data:
            return {"mean": None, "min": None, "max": None}
        return {
            "mean": sum(data) / len(data),
            "min": min(data),
            "max": max(data)
        }

# Example
cb = CircularBuffer(5)
cb.add(10)
cb.add(20)
cb.add(30)
cb.add(40)
cb.add(50)
cb.add(60)  

print("Últimos datos:", cb.get_latest())
print("Estadísticas:", cb.get_stats())
