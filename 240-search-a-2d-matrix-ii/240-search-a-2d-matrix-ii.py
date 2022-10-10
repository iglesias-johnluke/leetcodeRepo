class Solution:
    '''
   binary search on each row
    
    
    '''
    def search(self, row, target):
        l = 0
        r = len(row) - 1
        while l <= r:
            mid = (r+l)//2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                r = mid-1
            else:
                l = mid+1
        
        return False
        
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if self.search(row, target):
                return True
        
        return False
                
        
