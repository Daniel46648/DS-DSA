class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = pre

        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        temp = self.head
        if self.length <= 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.head = self.head.next
            temp.next = None
            self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value =value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if self.length == index:
            return self.append(value)

        temp = Node(value)
        pre = self.get(index - 1)

        temp.next = pre.next
        pre.next = temp
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if self.index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def remove_duplicates(self):
        if self.head is None or self.head.next is None:
            return self.head
        else:
            x = set()
            temp = self.head
            while temp.next is not None:
                if temp.next.value in x:
                    temp.next = temp.next.next
                    self.length -= 1
                else:
                    x.add(temp.next.value)
                    temp = temp.next

    def binary_to_decimal(self):
        num = 0
        if self.head is None:
            return None
        else:
            temp = self.head
            while temp is not None:
                if temp.value == 1:
                    num += 1
                if temp.next:
                    num = num * 2
                temp = temp.next
        return num

    def partition_list(self, x):
        if self.length == 0 or self.length == 1:
            return self.head
        else:
            d1 = Node(0)
            d2 = Node(0)
            prev1 = d1
            prev2 = d2
            temp = self.head
            while temp is not None:
                if temp.value < x:
                    prev1.next = temp
                    prev1 = prev1.next
                else:
                    prev2.next = temp
                    prev2 = prev2.next
                temp = temp.next
                
            prev1.next = d2.next
            prev2.next = None
            d2.next = None
            self.head = d1.next
            d1.next = None

    def reverse_between(self, start, end):
        if self.length <= 1:
            return None
        if start == 0:
            d = Node(0)
            d.next = self.head
            prev = d
        else:
            prev = self.head
        for i in range(start - 1):
            prev = prev.next
        current = prev.next
        for _ in range(end - start):
            to_move = current.next
            current.next = to_move.next
            to_move.next = prev.next
            prev.next = to_move
        if start == 0:
            self.head = d.next

    def swap_in_pairs(self):
        if self.length == 0 or self.length == 1:
            return self.head
        temp = self.head
        fast = temp.next
        pre = temp
        while fast.next:
            temp = temp.next
            temp.next = pre
            pre.next = fast
            fast = temp.next
            temp = pre

    def swap_pairs(self):
        if not self.head or not self.head.next:
            return self.head
        temp = self.head
        fast = temp
        d = Node(0)
        d.next = self.head
        pre = d
        while pre.next and pre.next.next:
            temp = pre.next
            fast = temp.next
            temp.next = fast.next
            fast.next = temp
            pre.next = fast
            pre = temp
        
        self.head = d.next
        d.next = None
            
#This is the end of my learning stage about pointers and LL in python