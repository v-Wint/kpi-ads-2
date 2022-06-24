from files_handling import read_file, write_file
from algorithm import solve_knapsack


def main():
    for i in [5, 10, 100]:
        write_file(f"files/output_{i}.txt", solve_knapsack(*read_file(f"files/input_{i}.txt")))


if __name__ == "__main__":
    main()
