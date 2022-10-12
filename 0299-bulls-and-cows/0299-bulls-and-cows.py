class Solution:
    
    '''
    map secret chars to list of indices in secretString
    GET BULLS
    loop thru guess:
        if char in secret.keys and index is in list at secret[char]:
            bulls+=1
            remove index from list
    
    GET COWS
    elif char in secret.keys and list of indices >= 1
        cows+=1
        remove min item from list
    return string
    '''
    def getHint(self, secret: str, guess: str) -> str:
        
        map = {}
        bulls = 0
        cows = 0
        bullIndices = set()
        for i in range(len(secret)):
            char = secret[i]
            if char in map.keys():
                map[char]+=1
            else:
                map[char] = 1
                
        for i in range(len(guess)):
            char = guess[i]
            if char in map.keys() and guess[i] == secret[i]:
                bulls +=1
                map[char]-=1
                bullIndices.add(i)
                
        for i in range(len(guess)):
            char = guess[i]
            if (i not in bullIndices) and char in map.keys() and map[char] >= 1:
                cows +=1
                map[char]-=1
        
        
        return str(bulls) + "A" + str(cows) + "B"
            
        
        
        
        
        
        
        