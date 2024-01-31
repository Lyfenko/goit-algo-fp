"""

Завдання 5. Візуалізація обходу бінарного дерева

Використовуючи код із завдання 4 для побудови бінарного дерева.
Необхідно створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.

Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0).
Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу.
Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.

"""

import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


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
            pos[node.left.id] = (x - 1 / 2**layer, y - 1)
            graph.add_edge(node.id, node.left.id)
            add_edges(
                graph, node.left, pos, x=x - 1 / 2**layer, y=y - 1, layer=layer + 1
            )
        if node.right:
            pos[node.right.id] = (x + 1 / 2**layer, y - 1)
            graph.add_edge(node.id, node.right.id)
            add_edges(
                graph, node.right, pos, x=x + 1 / 2**layer, y=y - 1, layer=layer + 1
            )


def draw_heap(heap_root, traversal_order):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    add_edges(heap, heap_root, pos)

    # Generate colors
    colors = list(mcolors.TABLEAU_COLORS.values())
    color_idx = 0

    for i, node_id in enumerate(traversal_order):
        heap.nodes[node_id]["color"] = colors[color_idx]
        color_idx = (color_idx + 1) % len(colors)

    labels = {node[0]: node[1]["label"] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        heap,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=list(nx.get_node_attributes(heap, "color").values()),
    )
    plt.show()


def dfs_traversal(node, traversal_order):
    if node:
        traversal_order.append(node.id)
        dfs_traversal(node.left, traversal_order)
        dfs_traversal(node.right, traversal_order)


def bfs_traversal(root, traversal_order):
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            traversal_order.append(node.id)
            queue.append(node.left)
            queue.append(node.right)


if __name__ == "__main__":
    # Створення бінарної купи
    root = Node(4, 1)
    root.left = Node(8, 2)
    root.right = Node(6, 3)
    root.left.left = Node(10, 4)
    root.left.right = Node(15, 5)
    root.right.left = Node(12, 6)

    # DFS
    dfs_order = []
    dfs_traversal(root, dfs_order)
    draw_heap(root, dfs_order)

    # BFS
    bfs_order = []
    bfs_traversal(root, bfs_order)
    draw_heap(root, bfs_order)
