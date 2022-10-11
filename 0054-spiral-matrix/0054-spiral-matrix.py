class Solution:
    '''
    traverse right, left, up, down outer part of matrix
    append to output
    after each traversal update rightBoundIndex, leftBoundIndex, topIndex, bottomIndex
    
    '''
    def goRight(self, output, startRow, startCol, rowBound, colBound, matrix):
        if not startCol <= colBound or not  startRow <= rowBound:
            return (startRow, startCol, rowBound, colBound)
        
        for j in range(startCol, colBound+1):
            output.append(matrix[startRow][j])
        return(startRow+1, startCol, rowBound, colBound)
    
    def goLeft(self, output, startRow, startCol, rowBound, colBound, matrix):
        if not startCol <= colBound or not  startRow <= rowBound:
            return (startRow, startCol, rowBound, colBound)
        
        for i in reversed(range(startCol, colBound+1)):
            output.append(matrix[rowBound][i])
        return (startRow, startCol, rowBound-1, colBound)
    
    def goUp(self, output, startRow, startCol, rowBound, colBound, matrix):
        if not startRow <= rowBound or not  startCol<= colBound:
            return (startRow, startCol, rowBound, colBound)
        
        for i in reversed(range(startRow, rowBound+1)) :
            output.append(matrix[i][startCol])
        return(startRow, startCol+1, rowBound, colBound)
    
    def goDown(self, output, startRow, startCol, rowBound, colBound, matrix):
        if not startRow <= rowBound or not  startCol<= colBound:
            return (startRow, startCol, rowBound, colBound)
        
        for i in range(startRow, rowBound+1):
            output.append(matrix[i][colBound])
        return (startRow, startCol, rowBound, colBound-1)
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        startRow, startCol, rowBound, colBound = 0, 0, len(matrix)-1, len(matrix[0])-1
        while len(output) < len(matrix) * len(matrix[0]):
            startRow, startCol, rowBound, colBound = self.goRight(output, startRow, startCol, rowBound, colBound, matrix)
            startRow, startCol, rowBound, colBound = self.goDown(output, startRow, startCol, rowBound, colBound, matrix)
            startRow, startCol, rowBound, colBound = self.goLeft(output, startRow, startCol, rowBound, colBound, matrix)
            startRow, startCol, rowBound, colBound = self.goUp(output, startRow, startCol, rowBound, colBound, matrix)
        return output
            
        
        
        
        
        
        
        
        
        