from collections import defaultdict, deque
from bigtree import Node

path_dict = {
    "1": {"name": "1"},
    "1/2": {"name": "2"},
    "1/3": {"name": "3"},
    "1/2/4": {"name": "4"},
    "1/2/5": {"name": "5"},
    "1/3/6": {"name": "6"},
    "1/3/7": {"name": "7"},
    "1/3/6/8": {"name": "8"},
    "1/3/7/9": {"name": "9"},
}

created_nodes = {"1": Node("1", data=path_dict["1"])}

for path, node_data in path_dict.items():
    if path != "1":
        nodes = path.split("/")
        current_node = created_nodes[nodes[0]]
        for node in nodes[1:]:
            if node not in created_nodes:
                created_nodes[node] = Node(node_data["name"], parent=current_node, data=path_dict[path])
            current_node = created_nodes[node]

created_nodes["1"].show(attr_list=["name"])


class Nodes:
    def __init__(self, current):
        self.current = current
        self.right = None
        self.left = None


def create_tree():
    root = Nodes(1)
    root.left = Nodes(2)
    root.right = Nodes(3)
    root.left.left = Nodes(4)
    root.left.right = Nodes(5)
    root.right.left = Nodes(6)
    root.right.right = Nodes(7)
    root.right.left.right = Nodes(8)
    root.right.right.right = Nodes(9)
    return root


def vertical_traversal(root):
    if not root:
        return []

    vertical_order = defaultdict(list)
    queue = deque()
    queue.append((root, 0))

    while queue:
        node, distance = queue.popleft()
        vertical_order[distance].append(node.current)

        if node.left:
            queue.append((node.left, distance + 1))
        if node.right:
            queue.append((node.right, distance - 1))

    sorted_dist = sorted(vertical_order.keys())

    result = []
    for distance in sorted_dist:
        result.extend(sorted(vertical_order[distance], reverse=True))

    return result


root = create_tree()
result = vertical_traversal(root)
print("=" * 30 + "\nOutput: ")
print(result)
