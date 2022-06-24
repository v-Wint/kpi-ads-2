def find_min_edge(matrix: list) -> ((int, int), int):
    n = len(matrix)
    min_l = matrix[0][1]
    edge = (0, 1)
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] < min_l:
                edge = (i, j)
                min_l = matrix[i][j]
    return edge, min_l


def find_next_node(matrix: list, node: int, path: list) -> (int, int):
    next_node = -1
    min_l = 9999999
    for i, length in enumerate(matrix[node]):
        if i != node and length < min_l and i not in path:
            min_l = length
            next_node = i
    return next_node, min_l


def greedy_traversal(matrix: list) -> (list, int):
    path, length = find_min_edge(matrix)
    path = list(path)
    node = path[-1]
    while len(matrix) != len(path):
        node, l = find_next_node(matrix, node, path)
        path.append(node)
        length += l
    length += matrix[path[0]][path[-1]]
    path.append(path[0])
    return path, length
