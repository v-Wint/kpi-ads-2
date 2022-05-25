class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


class MyList:
    def __init__(self, head=None):
        self.__head = head

    def __len__(self):
        cur = self.__head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError("list index out of range")
        cur = self.__head
        for _ in range(index):
            cur = cur.next
        return cur.data

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __repr__(self):
        return ", ".join(str(x) for x in self)

    def push(self, data):
        """Push element into the tail of the list"""
        node = Node(data)
        if len(self) == 0:
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node

    def pop(self, index):
        """Remove element with an index from a list"""
        if index >= len(self):
            raise IndexError("list index out of range")
        if index == 0:
            self.__head = self.__head.next
        else:
            cur = self.__head
            for _ in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
