#ejercicio8
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        """Añade un nodo al final de la lista."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def delete_from_position(self, position):
        """Elimina el nodo en la posición dada y devuelve su valor."""
        if not self.head or position < 0:
            return None  # Lista vacía o posición inválida
        if position == 0:
            deleted_data = self.head.data
            self.head = self.head.next
            return deleted_data
        current = self.head
        for _ in range(position - 1):
            if not current.next:  # Si la posición está fuera de rango
                return None
            current = current.next
        if not current.next:  # Si no hay nodo en la posición
            return None
        deleted_data = current.next.data
        current.next = current.next.next
        return deleted_data
    def display(self):
        """Muestra la lista como una cadena de nodos."""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")
# Pruebas
if __name__ == "__main__":
    lista = LinkedList()
    lista.append(10)
    lista.append(20)
    lista.append(30)
    print("Lista original:")
    lista.display()  # 10 -> 20 -> 30 -> None
    print("Nodo eliminado (posición 1):", lista.delete_from_position(1))  # Output: 20
    print("Lista actualizada:")
    lista.display()  # 10 -> 30 -> None
