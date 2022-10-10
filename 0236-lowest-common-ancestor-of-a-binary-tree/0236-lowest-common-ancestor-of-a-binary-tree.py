# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    '''
    check if p is q's parent, vice-versa
    traverse tree, update output if node is parent to both
        return node
    '''
    def hasChild(self, parent, node):
        q = deque()
        q.append(parent)
        while q:
            popped = q.popleft()
            if popped:
                if popped == node:
                    return True
                q.append(popped.left)
                q.append(popped.right)
        return False
        
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if self.hasChild(p, q):
            return p
        elif self.hasChild(q, p):
            return q
        queue = deque()
        queue.append(root)
        output = None
        while queue:
            popped = queue.popleft()
            if popped:
                queue.append(popped.left)
                queue.append(popped.right)
                if self.hasChild(popped, p) and self.hasChild(popped, q):
                    output = popped
        return output
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        