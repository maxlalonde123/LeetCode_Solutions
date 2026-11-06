# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        return mergeLists(lists)
    
def mergeLists (lists: list[ListNode | None]) -> ListNode | None:
    if len(lists) >= 2:
        if len(lists) > 2:
            left = mergeLists(lists[ : len(lists) // 2])
            right = mergeLists(lists[len(lists) // 2 : ])
        else:
            left = lists[0]
            right = lists[1]

        if left == None and right != None:
            return right
        elif right == None and left != None:
            return left
        elif left == None and right == None:
            return None

        if left.val <= right.val:
            head = ListNode(left.val, None)
            left = left.next
        else:
            head = ListNode(right.val, None)
            right = right.next

        current = head
        
        while left != None or right != None:
            if left == None:
                current.next = ListNode(right.val, None)
                right = right.next
            elif right == None:
                current.next = ListNode(left.val, None)
                left = left.next
            elif left.val <= right.val:
                current.next = ListNode(left.val, None)
                left = left.next
            else:
                current.next = ListNode(right.val, None)
                right = right.next

            current = current.next
        
        return head

    elif len(lists) == 1:
        return lists[0]
    
    else:
        return None