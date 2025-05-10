# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = ''
        num2 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        total = int(num1[::-1]) + int(num2[::-1])
        numbers = []
        if total == 0:
            numbers.append(total)
        else:
            while total > 0:
                numbers.insert(0, total % 10)
                total //= 10
        class LinkedList:
            def __init__(self):
                self.head = None
            def insert_values(self, items):
                for item in items:
                    self.head = ListNode(item, self.head)
                return self.head
        linked_list = LinkedList()
        
        return linked_list.insert_values(numbers)
        
