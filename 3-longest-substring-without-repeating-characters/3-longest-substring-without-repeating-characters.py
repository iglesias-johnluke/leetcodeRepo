
from collections import deque
class Solution:
    '''
    queue with curr unique string
    for each char
        if char in stack, keep popping front until duplicate popped, remove pops from set
        
        append char to q
        add char to set
        update longest string
    
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        currSet = set()
        longest = 0
        for char in s:
            if char in currSet:
                popped = q.popleft()
                currSet.remove(popped)
                while popped != char:
                    popped = q.popleft()
                    currSet.remove(popped)
            q.append(char)
            currSet.add(char)
            longest = max(longest, len(q))
        
        
        return longest
            
            