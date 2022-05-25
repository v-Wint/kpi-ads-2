def sort_count_inv(array: list) -> (list, int):
    """Count inversions within given array while doing merge sort
    :param array: given array
    :return: sorted array, number of inversions
    """
    n = len(array)
    if n == 1:
        return array, 0
    else:
        left, x = sort_count_inv(array[:n//2])
        right, y = sort_count_inv(array[n//2:])
        array, z = merge_count_split_inv(left, right)
        return array, x+y+z


def merge_count_split_inv(left: list, right: list) -> (list, int):
    """Count split inversions while merging two arrays
    We're using approach with creating a temporary array so that code is more pythonic

    :param left: left part of an array
    :param right: right part of an array
    :return: merged array and number of split inversions
    """
    temp = []
    c = i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
            c += (len(left) - i)
    temp += left[i:]
    temp += right[j:]
    return temp, c


def create_comparison_list(first_array: list, second_array: list) -> list:
    """Create an array to count inversions from two given rating arrays"""
    new_array = first_array.copy()
    for a, b in zip(first_array, second_array):
        new_array[a-1] = b
    return new_array
