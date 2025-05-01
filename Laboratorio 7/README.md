# 🧠 Algoritmos con Árboles Binarios en Python

Este repositorio contiene una serie de ejercicios de estructuras de datos centrados en **árboles binarios**, implementados en Python. Cada archivo aborda una operación común sobre árboles y viene acompañado de ejemplos o pruebas para verificar su correcto funcionamiento.

---

## 📁 Contenido

| Archivo         | Descripción                                      |
|-----------------|--------------------------------------------------|
| `ejercicio1.py` | Calcula la **altura** de un árbol binario        |
| `ejercicio2.py` | Cuenta las **hojas** (nodos sin hijos)           |
| `ejercicio3.py` | Invierte el árbol (lo convierte en su **espejo**)|
| `ejercicio4.py` | Realiza un **recorrido por niveles**             |
| `ejercicio5.py` | Verifica si el árbol está **balanceado**         |

---

## 📘 Detalles de cada ejercicio

### 🟦 `ejercicio1.py` – Altura del Árbol
Calcula la altura máxima (profundidad) de un árbol binario.

```python
def tree_height(root):
    if not root:
        return -1
    return 1 + max(tree_height(root.left), tree_height(root.right))

✔ Pruebas incluidas: árbol vacío, árbol con un solo nodo, árbol balanceado y árbol desbalanceado.

🟩 ejercicio2.py – Contar Hojas
Cuenta cuántos nodos hoja (sin hijos) hay en el árbol.

def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

🟨 ejercicio3.py – Árbol Espejo (Mirror)
Invierte (refleja) un árbol binario intercambiando sus hijos izquierdo y derecho.

def mirror_tree(node):
    if node is None:
        return None
    node.left, node.right = mirror_tree(node.right), mirror_tree(node.left)
    return node

🟧 ejercicio4.py – Recorrido por Niveles
Realiza un recorrido nivel por nivel del árbol y devuelve los valores por nivel.

def level_order_traversal(root):
    ...
    return result

🟥 ejercicio5.py – Árbol Balanceado
Verifica si un árbol binario está balanceado (diferencia de altura ≤ 1 entre subárboles de cada nodo).

def is_balanced(root):
    ...
✔ Pruebas incluidas: árbol balanceado, desbalanceado, árbol vacío y casos límite.

🧪 Cómo ejecutar
Asegúrate de tener Python 3 instalado. Luego, ejecuta cualquier archivo para ver sus resultados o pruebas:

python ejercicio1.py
python ejercicio2.py
python ejercicio3.py
python ejercicio4.py
python ejercicio5.py
📦 Requisitos
Python 3.6 o superior
No se requieren librerías externas (solo collections de la librería estándar)

👩‍💻 Autores
Milagros Madelein Ramos Chamorro
Mayela Milagros Ticona Mamani
Steven Salandaña
Wilson Lopez Aponte
Estudiante de TECSUP | Apasionados por la lógica, estructuras de datos y el aprendizaje autodidacta.

📄 Licencia
Este proyecto está bajo la Licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente para fines educativos o personales.









