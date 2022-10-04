class Solution:
    '''
    recursively keep splitting list in half
    stop splitting when nums is empty or length nums == 1
    
    merge each split array by using 2 pointers to sort
    
    
    '''
    def helper(self, arr):
        length = len(arr)
        output = [0] * length
        if length == 0 or length == 1:
            return arr
        
        mid = (length)//2
        leftSide = self.helper(arr[:mid])
        rightSide = self.helper(arr[mid:])
        
        #merge lists
        lp = 0
        rp = 0
        currIndex = 0
        while lp < len(leftSide) and rp < len(rightSide):
            if leftSide[lp] < rightSide[rp]:
                output[currIndex] = leftSide[lp]
                lp+=1
            else:
                output[currIndex] = rightSide[rp]
                rp+=1
            currIndex +=1
            
        while lp < len(leftSide):
            output[currIndex] = leftSide[lp]
            lp+=1
            currIndex +=1
        while rp < len(rightSide):
            output[currIndex] = rightSide[rp]
            rp+=1
            currIndex +=1
        return output
        
            
    
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.helper(nums)