def floyd_algorithm(matrix: list) -> (list, list):
    """Conducts floyd algorithm, returns matrix of the smallest paths and matrix of next nodes"""
    next_nodes = [[-1 for _ in range(len(matrix))] for _ in range(len(matrix))]
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    next_nodes[i][j] = k
    return matrix, next_nodes


def get_path(i: int, j: int, next_nodes: list, path: list) -> None:
    """Recreate path using next nodes list, adds only nodes inbetween"""
    k = next_nodes[i][j]
    if k == -1:
        return
    get_path(i, k, next_nodes, path)
    path.append(k)
    get_path(k, j, next_nodes, path)
