from LL import Linkedlist, Node
#find middle Node without knowing about self.length
class Solution:
    def find_middle_node(self):
        slow = self.head
        fast = slow
        while fast != self.tail and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def has_loop(self):
        slow = self.head
        fast = slow
        while fast != None and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        else:
            return False