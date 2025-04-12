class DynamicArrayStack:
    """Stack implementation using a dynamic array that resizes when full."""
    
    def __init__(self, initial_capacity=10):
        """Initialize empty stack with dynamic capacity."""
        self.data = [None] * initial_capacity
        self.capacity = initial_capacity
        self.top = -1
        self.initial_capacity = initial_capacity  # Guarda la capacidad inicial
    
    def is_empty(self):
        """Check if stack is empty."""
        return self.top == -1
    
    def resize(self, new_capacity):
        """Resize the stack to a new capacity."""
        new_data = [None] * new_capacity
        
        # Copiar elementos al nuevo array
        for i in range(self.top + 1):
            new_data[i] = self.data[i]
            
        self.data = new_data
        self.capacity = new_capacity
    
    def push(self, item):
        """Añadir item al tope del stack."""
        if self.top == self.capacity - 1:
            # Duplicar capacidad si está lleno
            self.resize(2 * self.capacity)
        
        self.top += 1
        self.data[self.top] = item
        return True
    
    def pop(self):
        """Remover y retornar el item del tope."""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty")
        
        item = self.data[self.top]
        self.data[self.top] = None  # Eliminar referencia
        self.top -= 1
        
        # Reducir capacidad si es 1/4 del total y mayor que la inicial
        if (0 < self.top + 1 <= self.capacity // 4 
            and self.capacity > self.initial_capacity):
            self.resize(self.capacity // 2)
            
        return item
    
    # Los demás métodos (peek, size, __str__) permanecen igual
    
    def peek(self):
        """Retornar el tope sin removerlo."""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty")
        return self.data[self.top]
    
    def size(self):
        """Número de elementos en el stack."""
        return self.top + 1
    
    def __str__(self):
        """Representación en cadena del stack."""
        if self.is_empty():
            return "Stack: []"
        items = [str(self.data[i]) for i in range(self.top + 1)]
        return f"Stack: [{', '.join(items)}]"


def test_dynamic_array_stack():
    """Test dynamic array stack with auto-resizing."""
    print("Test: Dynamic array stack with auto-resizing")
    stack = DynamicArrayStack(3)  # Capacidad inicial pequeña
    
    print(f"Initial capacity: {stack.capacity}")
    
    # Añadir elementos más allá de la capacidad inicial
    for i in range(1, 8):
        stack.push(i)
        print(f"After push({i}): size={stack.size()}, capacity={stack.capacity}")
    
    # Remover elementos para activar reducción
    for _ in range(6):
        val = stack.pop()
        print(f"After pop -> {val}: size={stack.size()}, capacity={stack.capacity}")
    
    print("All dynamic array stack tests passed!")


if __name__ == "__main__":
    test_dynamic_array_stack()
