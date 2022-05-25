def euler_rec(matrix, node, path):
    """Recursive function to conduct DFS checking if an edge is already in the path"""
    for i in range(len(matrix[0])):
        if matrix[node][i]:
            for next_node in range(len(matrix)):
                # find edge, check if in the path
                if matrix[next_node][i] and next_node != node \
                        and (node, next_node) not in path and (next_node, node) not in path:
                    path.append((node, next_node))
                    euler_rec(matrix, next_node, path)
                    return


def find_euler_cycle(matrix):
    """Find euler path and return a list of nodes you need to go through"""
    # check for having an euler cycle and find the node with the greatest degree
    m = 0
    node = 0
    for i, line in enumerate(matrix):
        s = sum(line)
        if s % 2 == 1:
            return []
        if s > m:
            node = i
            m = s

    path = []
    # start recursive DFS
    euler_rec(matrix, node, path)
    return path
