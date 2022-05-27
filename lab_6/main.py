from random import randint
from algorithm import Node


def main():
    # --- Generating random graph ---
    root = Node(randint(-500, 1000))

    for _ in range(randint(2, 3)):
        root.append(Node(randint(-1000, 1000)))

    for child in root.children:
        for _ in range(randint(1, 3)):
            child.append(Node(randint(-500, 1000)))
        for ch in child.children:
            for _ in range(randint(1, 3)):
                ch.append(Node(randint(-500, 1000)))

    print("Before: \n", root)

    root.swap_max_min()

    print("After: \n", root)


if __name__ == "__main__":
    main()
