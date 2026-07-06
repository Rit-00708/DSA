# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a "dummy" node. This gives us a convenient starting point
        # to attach our merged nodes to, without worrying about edge cases
        # like an initially empty merged list.
        dummy = ListNode(-1)
        
        # 'current' will act as our tail pointer, building the new list node by node
        current = dummy
        
        # Traverse both lists as long as neither is empty
        while list1 and list2:
            if list1.val <= list2.val:
                # If list1's value is smaller, attach it to our merged list
                current.next = list1
                # Move list1's pointer to its next node
                list1 = list1.next
            else:
                # If list2's value is smaller, attach it to our merged list
                current.next = list2
                # Move list2's pointer to its next node
                list2 = list2.next
                
            # Move our current pointer forward to the newly attached node
            current = current.next
            
        # Once one list is exhausted, simply attach the remaining nodes of the other list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
            
        # The merged list starts immediately after our dummy node
        return dummy.next