# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    '''
    traverse both lists, append to num1, num2 strings
    reverse both strings, convert to int, sum
    convert sum to str, reverse str
    create new list for each char in str
    '''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        curr = l1
        while curr:
            num1 += str(curr.val)
            curr = curr.next
        curr = l2
        while curr:
            num2 += str(curr.val)
            curr = curr.next
            
        num1 = int(num1[::-1])
        num2 = int(num2[::-1])
        
        totalStr = (str(num1 + num2))[::-1]
        
        output = None
        for char in totalStr:
            if not output:
                output = ListNode(char)
                prev = output
            else:
                newNode = ListNode(char)
                prev.next = newNode
                prev = newNode
                
                
        
        return output
        
        
        
        
        
        