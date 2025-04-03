#ejercicio7
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
    def delete_from_end(self):
        """Elimina el último nodo de la lista y devuelve su valor."""
        if not self.head:
            return None  # Lista vacía
        if not self.head.next:
            deleted_data = self.head.data
            self.head = None
            return deleted_data
        current = self.head
        while current.next.next:
            current = current.next
        deleted_data = current.next.data
        current.next = None
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
    print("Nodo eliminado:", lista.delete_from_end())  # Output: 30
    print("Lista actualizada:")
    lista.display()  # 10 -> 20 -> None
