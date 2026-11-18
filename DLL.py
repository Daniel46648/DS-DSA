class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        temp = self.tail
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        self.tail = temp.prev
        temp.prev.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, - 1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.get(index)
        new_node = Node(value)
        pre = temp.prev
        pre.next = new_node
        new_node.next = temp
        temp.prev = new_node
        new_node.prev = pre

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def palindrome_check(self):
        if self.length <= 1:
            return True
        fw = self.head
        bw = self.tail
        while fw != bw and fw.prev != bw:
            if bw.value != fw.value:
                return False
            bw = bw.prev
            fw = fw.next
        return True

    def reverse(self):
        if self.length == 0:
            return False
        if self.length == 1:
            return True
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        quick = self.head
        self.head = self.tail
        self.tail = quick
        quick.next = None
        return True

    def partition_list(self, x):
        if self.length <= 1:
            return False
        D1 = Node(0)
        D2 = Node(0)
        pre = D1
        pre2 = D2
        cur = self.head
        while cur:
            nxt = cur.next
            cur.prev = None
            cur.next = None
            if cur.value < x:
                cur.prev = pre
                pre.next = cur
                pre = pre.next
            else:
                cur.prev = pre2
                pre2.next = cur
                pre2 = pre2.next
            cur = nxt
        if D1.next is None:
            self.head = D2.next
            self.head.prev = None
            self.tail = pre2
            return True

        self.head = D1.next
        self.head.prev = None

        if D2.next is not None:
            pre.next = D2.next
            D2.next.prev = pre
            self.tail = pre2
        else:
            self.tail = pre
        D1.next = None
        D2.next = None
        return True

    def reverse_between(self, start_index, end_index):
        if start_index < 0:
            return False
        if start_index >= self.length:
            return False
        if self.length == 0:
            return False
        if self.length == 1:
            return True
        if end_index >= self.length or start_index > end_index:
            return False
        if start_index == end_index:
            return True

        if start_index == 0:
            d1 = Node(0)
            d1.next = self.head
            self.head.prev = d1
        temp = self.head
        for _ in range(start_index):
            temp = temp.next
        start_node = temp
        before = temp.prev

        last_reversed = None
        for _ in range(end_index - start_index + 1):
            last_reversed = temp
            pre = temp.prev
            temp.prev = temp.next
            temp.next = pre
            temp = temp.prev
        before.next = last_reversed
        last_reversed.prev = before

        start_node.next = temp
        if temp:
            temp.prev = start_node

        if end_index == self.length - 1:
            self.tail = start_node

        if start_index == 0:
            self.head = d1.next
            self.head.prev = None
            d1.next = None
        return True

    def swap_pairs(self):
        if self.length <= 1:
            return False
        temp = self.head
        self.head = self.head.next
        self.head.prev = None

        while temp and temp.next:
            cur = temp.next
            temp.next = cur.next
            cur.next = temp
            cur.prev = temp.prev
            temp.prev = cur

            if cur.prev:
                cur.prev.next = cur
            temp = temp.next
            if temp:
                temp.prev = cur.next
        return True
