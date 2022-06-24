import sys


def read_file(file_name: str) -> (int, list, list):
    """Read information for solvign knapsakc problem from file:
    Max weight, list of weights, list of values"""
    try:
        with open(file_name, 'r') as f:
            W = int(f.readline().split()[0])
            lines = list(map(lambda x: x.split(), f.readlines()))
            values = list(map(lambda x: int(x[0]), lines))
            weights = list(map(lambda x: int(x[1]), lines))
            return W, weights, values
    except FileNotFoundError:
        print(f"FILE NOT FOUND: {file_name}")
        sys.exit(-1)


def write_file(file_name: str, data: int) -> None:
    with open(file_name, 'w') as f:
        f.write(str(data))
