from algorithm import MyList
from random import choice


def main():
    my_list = MyList()

    n = int(input("Number of elements: "))

    for _ in range(n):
        my_list.push(choice(range(n)))

    print("Original list: ", my_list)

    evens = 0
    for i in range(len(my_list)-1, -1, -1):
        if my_list[i] % 2 == 0:
            my_list.pop(i)
            evens += 1

    print(f"Number of removed even numbers: {evens}")

    print("Changed list: ", my_list)


if __name__ == "__main__":
    main()
