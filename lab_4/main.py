from algorithm import floyd_algorithm, get_path
from random import choice
import graph_examples
INF = 9999


def create_random_graph(n):
    print("Random Graph: ")
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = choice([INF, choice(range(1, 101))])

            print(matrix[i][j] if matrix[i][j] != INF else "inf", end="\t\t")
        print()
    return matrix


def process_graph(matrix):
    results, next_nodes = floyd_algorithm(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if results[i][j] != INF and i != j:  # get_path doesn't check if INF between two nodes
                path = [i]
                get_path(i, j, next_nodes, path)
                path.append(j)
                print(" -> ".join(str(x) for x in path))
                print(f"Weight: {results[i][j]}")


def main():
    process_graph(create_random_graph(int(input("Enter number of edges: "))))
    # process_graph(graph_examples.my_graph)


if __name__ == "__main__":
    main()


























