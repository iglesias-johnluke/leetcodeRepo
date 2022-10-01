class Solution:
    
    '''
    map values to symbols
    add 6 subtraction pairs to map
    
    num int -> string
    loop backwards in int string:
        increment numZeros
        add numZeros at current digit
        currRomanNumeral = ""
        while currNum !=0:
            if currNum in map.values:
                append roman numeral to currRomanNumeral
                currNum = 0
            else:
                currNum -= nextMapValue < currNum
                append to currRomanNumeral
            prepend currRomanNumeral to output
        
        numZeros += 1
            
    return output
    '''
    
    def nextMapValue(self, currValue, map):
        keys = []
        for k in map.keys():
            keys.append(k)
        keys.sort()
        keys.reverse() #descending keys
        for k in keys:
            if k <= currValue:
                return k
        return None
        
    
    
    def intToRoman(self, num: int) -> str:
        map = {
            1:"I",
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            1000:"M",
            4:"IV",
            9:"IX",
            40:"XL",
            90:"XC",
            400:"CD",
            900:"CM",
            500:"D"
        }
        
        numStr = str(num)
        zeros = ""
        output = ""
        for i in reversed(range(len(numStr))):
            currValue = int(numStr[i] + zeros)
            currRomanNumeral = ""
            
            while currValue != 0:
                if currValue in map.keys():
                    currRomanNumeral += map[currValue]
                    break
                else: #when currValue > keys in map
                    nextMapVal = self.nextMapValue(currValue, map)
                    currRomanNumeral += map[nextMapVal]
                    currValue -= nextMapVal
                        
            
            
            output = currRomanNumeral + output
            zeros += "0"
        
        return output 
        
        
        
        
        
        
        
        