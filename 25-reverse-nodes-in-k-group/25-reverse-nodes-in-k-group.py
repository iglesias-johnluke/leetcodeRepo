# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
reverseNodes()
    reverses nodes starting from node if length from node >= k
    else dont reverse
    
    return newHead, newTail, nextNode

keep calling reverseNodes until nextNode is None
after each reversal, connect newTail to head of next reverse

'''
class Solution:
    def hasK(self, head, k):
        count = 0
        curr = head
        while curr:
            count += 1
            if count >= k:
                return True
            curr = curr.next
        
        
        return False
    
    def getTail(self, head):
        curr = head
        prev = None
        while curr:
            prev = curr
            curr = curr.next
        return prev
            
    
    def reverseNodes(self, head, k):
        if not head:
            return (None, None, None)
        elif not self.hasK(head, k):
            tail =  self.getTail(head)
            return (head, tail, None)
        
        #reverse k nodes
        newTail = head
        
        curr = head
        prev = None
        count = 0
        while count < k:
            next = curr.next
            curr.next = prev
            
            prev = curr
            curr = next
            count += 1
        
        newHead = prev
        nextNode = curr
        return (newHead, newTail, nextNode)
        
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #connect each reversal
        if not head:
            return head
        elif head and not head.next:
            return head
        newHead, newTail, nextNode = self.reverseNodes(head, k)
        output = newHead
        
        while nextNode:
            tmpTail = newTail
            tmpNext = nextNode
            
            h, newTail, nextNode = self.reverseNodes(tmpNext, k)
            tmpTail.next = h
            
        
        
        return output
                
                
                
                
                
                
                
                
                
                
        