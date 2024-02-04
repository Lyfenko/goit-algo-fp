"""

Завдання 4. Візуалізація піраміди

Наступний код виконує побудову бінарних дерев. Виконайте аналіз коду, щоб зрозуміти, як він працює.
Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.

"""

import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer # noqa
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1) # noqa
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1) # noqa
    return graph


def draw_heap_tree(heap_array): # noqa
    # Побудова дерева з купи
    heap_tree_root = build_heap_tree(heap_array)

    tree = nx.DiGraph()
    pos = {heap_tree_root.id: (0, 0)}
    tree = add_edges(tree, heap_tree_root, pos, layer=0)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def build_heap_tree(heap_array, index=0): # noqa
    if index < len(heap_array):
        root_val = heap_array[index]
        root = Node(root_val)

        left_child_idx = 2 * index + 1
        right_child_idx = 2 * index + 2

        root.left = build_heap_tree(heap_array, left_child_idx)
        root.right = build_heap_tree(heap_array, right_child_idx)

        return root


if __name__ == "__main__":
    heap_array = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
    heapq.heapify(heap_array)

    draw_heap_tree(heap_array)
