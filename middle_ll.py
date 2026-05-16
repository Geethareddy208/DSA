# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowp=head
        fastp=head
        while (fastp!=None and fastp.next!=None):
            fastp=fastp.next.next
            slowp=slowp.next
        return slowp
        