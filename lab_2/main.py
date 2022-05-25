from algorithm import sort_count_inv, create_comparison_list
from filehandling import read_file, write_results, generate_random_file

COMPARED_USER_INDEX = 6


def process_data(entry_data: list) -> list:
    results = []

    for i, value in enumerate(entry_data):
        results.append(
            [i + 1, sort_count_inv(create_comparison_list(entry_data[COMPARED_USER_INDEX - 1][1:], value[1:]))[-1]])
    return results


def main():
    entry_file_name = "files/ip-12_Melnyk_02.txt"
    output_file_name = entry_file_name.replace(".txt", "_output.txt")

    # generate_random_file(entry_file_name)
    entry_data = read_file(entry_file_name)

    results = process_data(entry_data)
    write_results(output_file_name, results, COMPARED_USER_INDEX)


if __name__ == "__main__":
    main()
