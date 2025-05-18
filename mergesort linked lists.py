# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def merge_sort(ll):
            if not ll or not ll.next :
                return ll
            slow = ll
            fast = ll.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            right = slow.next
            slow.next = None
            left = merge_sort(ll)
            right = merge_sort(right)
            return sort_sorted_lists(left, right)
        def sort_sorted_lists(ll1, ll2):
            sorting_list = ListNode()
            tail = sorting_list
            while ll1 and ll2:
                if ll1.val <= ll2.val:
                    tail.next = ll1
                    ll1 = ll1.next
                else:
                    tail.next = ll2
                    ll2 = ll2.next
                tail = tail.next
            tail.next = ll1 or ll2
            return sorting_list.next
        list1 = merge_sort(list1)
        print(list1)
        list2 = merge_sort(list2)
        print(list2)
        
        return sort_sorted_lists(list1, list2)
