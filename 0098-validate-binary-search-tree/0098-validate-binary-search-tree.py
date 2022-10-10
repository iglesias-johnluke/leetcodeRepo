# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
check at each node if left subtree < node and right tree > node
'''
from collections import deque

class Solution:
    def isValid(self, node):
        q = deque()
        if not node:
            return True
        q.append(node.left)
        while q:
            popped = q.popleft()
            if popped:
                if popped.val >= node.val:
                    return False
                q.append(popped.left)
                q.append(popped.right)
                
        q = deque()
        q.append(node.right)
        while q:
            popped = q.popleft()
            if popped:
                if popped.val <= node.val:
                    return False
                q.append(popped.left)
                q.append(popped.right)
        return True
        
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        while q:
            popped = q.popleft()
            if popped:
                if not self.isValid(popped):
                    return False
                q.append(popped.left)
                q.append(popped.right)
        
        
        return True
        
        
        
        
        
        
        
        