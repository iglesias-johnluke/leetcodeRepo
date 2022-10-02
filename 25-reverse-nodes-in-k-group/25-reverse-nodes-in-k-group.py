# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    handle empty head
    can list be circular
    
    flip(node, k) reverses list if applicable, returns (newHead, newTail, nextNode)
    after each flip assign newTail.next = nextFlipHead
    keep flipping until nextNode == None or nextNode == head
    '''
    
    def canReverse(self, node, k):
        count = 0
        curr = node
        while curr and count < k:
            curr = curr.next
            count += 1
            
        return count == k
        
    def getTail(self, node):
        prev = None
        curr = node
        while curr:
            prev = curr
            curr = curr.next
        return prev
        
        
        
    def flip(self, node, k): #returns new head, next node
        if not node:
            return (None, None, None)
        elif not self.canReverse(node, k):
            return (node, self.getTail(node), None)
        count = 0
        curr = node
        prev = None
        nextNode = None
        while count < k and curr:
            nextNode = curr.next
            curr.next = prev
            
            prev = curr
            curr = nextNode
            count +=1
        
        return (prev, node, nextNode)
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        newHead, newTail, nextNode = self.flip(head, k)
        while nextNode:
            h, t, n = self.flip(nextNode, k)
            newTail.next = h
            
            nextNode = n
            newTail = t
        return newHead
            
            
            
            
                
                
                
                
                
                
                
                
                
                
        