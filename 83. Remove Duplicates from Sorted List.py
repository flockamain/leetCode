"""Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        curr = head
        if not head:
            return None
        elif head.next is None:
            return head
        #get to the second to last element in the linked list
        while head.next.next is not None:
            print(head.val)
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        if head.val == head.next.val:
            head.next = None

        return curr

        