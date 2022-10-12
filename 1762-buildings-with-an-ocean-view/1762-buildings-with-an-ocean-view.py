class Solution:
    '''
    traverse list, use stack
    when we reach height >= top of stack and stack populated, 
        keep popping from stack until top > curr
    add curr to stack
    '''
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i in range(len(heights)):
            while stack and heights[ stack[-1] ] <= heights[i]:
                stack.pop()
            stack.append(i)
                    
            
        return stack
        
        
        
                