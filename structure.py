class Node:

    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.value = value


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __shift(self, x):
        if self.first is None:
            self.first = Node(x)
            self.last = self.first
        else:
            new_first = Node(x, None, self.first)
            self.first.prev = new_first
            self.first = new_first

        self.length += 1

    def __push(self, x):
        if self.first is None:
            self.first = Node(x)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, self.first)
            self.first.next = self.last
        else:
            new_last = Node(x, self.last)
            self.last.next = new_last
            self.last = new_last

        self.length += 1

    def __unshift(self):
        old_first = self.first

        if old_first is None:
            return None

        self.first = old_first.next
        if self.first is None:
            self.last = None
        else:
            self.first.prev = None

        return old_first.value

    def __pop(self):
        if self.last is None:
            return None
        else:
            old = self.last
            self.last = old.prev
            self.last.next = None
            return old

    def insert(self, x):
        if self.first is None or self.first.value > x:
            self.__shift(x)
        elif self.last.value < x:
            self.__push(x)
        else:
            old = current = self.first
            while current is not None:
                if current.value > x:
                    node = Node(x, old, current)
                    current.prev = node
                    old.next = node
                    return
                old = current
                current = current.next

    def delete(self, x):
        if self.first is None:
            return None
        elif self.first.value == x:
            return self.__unshift()
        elif self.last.value == x:
            return self.__pop()
        else:
            current = self.first.next
            while current is not None:
                if current.value == x:
                    current.prev.next = current.next.prev
                    return current
                current = current.next

    def delete_max(self):
        return self.__pop()

    def delete_min(self):
        return self.__unshift()
