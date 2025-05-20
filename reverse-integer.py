class Solution(object):
    def reverse(self, x):
        num_string = str(x)
        class Node:
            def __init__(self, data=None, next=None):
                self.data = data
                self.next = next
        class LinkedList:
            def __init__(self):
                self.head = None
            def insert_at_end(self, item):
                if self.head == None:
                    self.head = Node(item, None)
                    return
                itr = self.head
                while itr.next:
                    itr = itr.next
                itr.next = Node(item, None)
            def remove_last(self):
                if self.head == None:
                    return self.head
                itr = self.head
                while itr.next.next:
                    itr = itr.next
                itr.next = None
            def insert_at_beginning(self, item):
                if self.head == None:
                    self.head = Node(item, None)
                    return
                self.head = Node(item, self.head)
            def append_values(self):
                itr = self.head
                new_string = ''
                while itr:
                    new_string += itr.data
                    itr = itr.next
                return new_string
        linked_list = LinkedList()
        for num in num_string:
            linked_list.insert_at_beginning(num)
        if x < 0:
            linked_list.remove_last()
            num = linked_list.append_values()
            num = int(num) - int(num) * 2
            if num > (2**31) - 1 or num < -2**31:
                return 0 
            return num 
        num = int(linked_list.append_values())
        if num > (2**31) - 1 or num < -2**31:
            return 0 
        return num