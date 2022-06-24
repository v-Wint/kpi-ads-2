from files_handling import matrix_from_file, write_results
from algorithm import greedy_traversal


def main():
    for i in range(1, 9):
        write_results(f"files/output_0{i}.txt",
                      *greedy_traversal(matrix_from_file(f"files/input_0{i}.txt")))


if __name__ == "__main__":
    main()
