import sys


def get_length(x1: int, x2: int, y1: int, y2: int) -> int:
    return int(((x1 - x2)**2 + (y1 - y2)**2)**0.5)


def matrix_from_file(file_name: str) -> list:
    try:
        with open(file_name, 'r') as f:
            n = int(f.readline())
            matrix = [[0 for _ in range(n)] for _ in range(n)]
            coords = [[int(l[0]), int(l[1])] for l in [line.split() for line in f.readlines()]]
            for i, first_line in enumerate(coords):
                for j, second_line in enumerate(coords):
                    matrix[i][j] = get_length(first_line[0], second_line[0], first_line[1], second_line[1])
            return matrix
    except FileNotFoundError:
        print(f"FILE NOT FOUND: {file_name}")
        sys.exit(-1)


def write_results(file_name: str, path: list, length: int) -> None:
    with open(file_name, 'w') as f:
        print(length, file=f)
        print(" ".join(str(x) for x in path), file=f)
