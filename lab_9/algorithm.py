def solve_knapsack(W: int, weights: list, values: list) -> int:
    """
    Algorithm to solve the knapsack problem using dynamic programming
    :param W: max weight
    :param weights: list of weights of items
    :param values: list of values of items
    :return: max value
    """
    n = len(values)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif weights[i - 1] <= j:
                table[i][j] = max(values[i - 1] + table[i - 1][j - weights[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]

    return table[n][W]
