"""Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]


Finally figured out linked lists in python!!! I got the general idea, but leetcode makes linked list problems in python really hard because it
gives the inputs as lists instead of creating the linked lists.

Need something like curr that copies the original point in memory to reference and output the entire linked list.

setting .next to .next.next essentially removes the link to the next value/point in memory. I believe this creates memory leaks though because
the original .next is still in memory, no? Need to do more research on that.

Removed print statement for better runtime and memory"""

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
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        if head.val == head.next.val:
            head.next = None

        return curr

        
