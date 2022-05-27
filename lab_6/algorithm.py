class Node:
    def __init__(self, value):
        self.value = value
        self.depth = 0
        self.children = []

    def append(self, node) -> None:
        node.depth = self.depth + 1
        self.children.append(node)

    def __repr__(self):
        s = '    '*self.depth + '|>> '
        s += str(self.value) + '\n'

        if self.children:
            for child in self.children:
                s += repr(child)
        return s

    def traversal(self, node) -> list:
        res = []

        if node:
            res.append(node)
            for child in node.children:
                res += self.traversal(child)

        return res

    def swap_max_min(self) -> None:
        nodes = self.traversal(self)
        min_node = max_node = nodes[0]
        for node in nodes[1:]:
            if node.value < min_node.value:
                min_node = node
            if node.value > max_node.value:
                max_node = node

        max_node.value, min_node.value = min_node.value, max_node.value
