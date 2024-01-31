"""

Завдання 4. Візуалізація піраміди

Наступний код виконує побудову бінарних дерев. Виконайте аналіз коду, щоб зрозуміти, як він працює.
Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.

"""

import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, index, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.index = index
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=f"{node.val}\n({node.index})")
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]["color"] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


if __name__ == "__main__":
    # Створення бінарної купи
    heap_root = Node(4, 1)
    heap_root.left = Node(8, 2)
    heap_root.right = Node(6, 3)
    heap_root.left.left = Node(10, 4)
    heap_root.left.right = Node(15, 5)
    heap_root.right.left = Node(12, 6)

    # Відображення бінарної купи
    draw_heap(heap_root)
