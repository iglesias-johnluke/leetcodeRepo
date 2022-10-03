# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    '''
    handle empty root, only one node
    traverse both subtrees, left tree we add leftChild, rightChild to tree
    do opposite for right tree
    check if both lists are equal
    
    '''
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True
        q1 = deque()
        q2 = deque()
        visited1 = []
        visited2 = []
        q1.append(root.left)
        q2.append(root.right)
        
        while q1:
            popped = q1.popleft()
            visited1.append(popped.val) if popped else visited1.append(None)
            if popped:
                q1.append(popped.left)
                q1.append(popped.right)
        while q2:
            popped = q2.popleft()
            visited2.append(popped.val) if popped else visited2.append(None)
            if popped:
                q2.append(popped.right)
                q2.append(popped.left)
        length = len(visited1)
        if length != len(visited2):
            return False
        for i in range(length):
            if visited1[i] != visited2[i]:
                return False
        
        return True
        
        
        
        
        
        