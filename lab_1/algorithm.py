from random import sample


def bubble_sort(A):
    num_of_swaps, num_of_comps = 0, 0
    for _ in range(len(A)-1):
        for i in range(len(A)-1):
            num_of_comps += 1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                num_of_swaps += 1
    print(f"Length: {len(A)}" )
    print(f"Number of comparisons: {num_of_comps}")
    print(f"Number of swaps {num_of_swaps}")
    return A, num_of_comps, num_of_swaps


def test_buble_sort():
    arr = sample(list(range(100)), 100)
    print(f"Initial array: {arr}")
    print(f"Sorted array: {bubble_sort(arr)[0]}")


def comb_sort(A):
    num_of_swaps, num_of_comps= 0, 0
    f = 1.2473309
    step = len(A) - 1
    while step >= 1:
        for i in range(len(A)-step):
            num_of_comps += 1
            if A[i] > A[i+step]:
                A[i], A[i+step] = A[i+step], A[i]
                num_of_swaps += 1
        step = int(step/f)
    print(f"Length: {len(A)}")
    print(f"Number of comparisons: {num_of_comps}")
    print(f"Number of swaps {num_of_swaps}")
    return A, num_of_comps, num_of_swaps


def test_comb_sort():
    arr = sample(list(range(100)), 100)
    print(f"Initial array: {arr}")
    print(f"Sorted array: {comb_sort(arr)[0]}")


if __name__ == "__main__":
    test_buble_sort()
    test_comb_sort()
