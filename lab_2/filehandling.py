from random import sample


def read_file(file_name: str) -> list:
    """
    Read input file
    :param file_name: path to the file
    :return: input data from the file or from randomly generated file if it doesn't exist
    """
    res = []
    try:
        with open(file_name) as f:
            line = f.readline().split()
            for i in range(int(line[0])):
                line = [int(i) for i in f.readline().split()]
                if line:
                    res.append(line)
    except FileNotFoundError:
        print("File doesn't exist, generating...")
        generate_random_file(file_name)
    return res


def write_results(file_name: str, data: list, compared: int) -> None:
    """Write output data to file in the according format"""
    with open(file_name, 'w') as f:
        print(compared, file=f)
        for user, similarity in sorted(data, key=lambda x: x[1]):
            if user != compared:
                print(user, similarity, file=f)
        print(compared, file=f)


def generate_random_file(file_name: str, users_n: int = 10, films_n: int = 5) -> None:
    """Generate random input file"""
    with open(file_name, 'w+') as f:
        print(f"{users_n} {films_n}", file=f)
        for i in range(1, users_n + 1):
            print(f"{i} {' '.join([str(x) for x in sample(range(1, films_n+1), films_n)])}", file=f)
