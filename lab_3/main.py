from algorithm import *


def input_to_matrix():
    matrix = []
    n = int(input("Number of nodes: "))
    print("Enter your graph:")
    for _ in range(n):
        line = []
        for char in input().strip():
            if char == "0":
                line.append(0)
            if char == "1":
                line.append(1)
        matrix.append(line)
    return matrix


def main():
    res = find_euler_cycle(input_to_matrix())
    if res:
        print(" -> ".join(str(edge[0]) for edge in res))
    else:
        print("No Euler cycle in the graph")


if __name__ == "__main__":
    main()
