"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

'''
handle cyclic list, empty pointer

map1 (original nodes) to new nodes with vals initialized
loop thru key nodes, check if nextNode == head
    map[originalNode].next = map[originalNode.next]
    if originalNode.random:
        map[originalNode].random = originalNode.random
return map1[originalHEad]
'''

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        map = {}
        map[head] = Node(head.val)
        curr = head
        
        while curr.next and curr.next != head: #populate map
            curr = curr.next
            map[curr] = Node(curr.val)
        
        if head.next:
            map[head].next = map[head.next]
        if head.random != None:
            map[head].random = map[head.random]
        
        curr = head.next
        while curr and curr != head:
            if curr.next:
                map[curr].next = map[curr.next]
            if curr.random:
                map[curr].random = map[curr.random]
            curr = curr.next
            
        return map[head]
        
        
        
        
        
        
        
        
        