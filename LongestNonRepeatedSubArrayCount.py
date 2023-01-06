def solution(string):
        longestSubArrayCount = 0
        length = len(string)
        i = 0
        
        while i < length:
            count = countLongestArray(string,i)
            if count > longestSubArrayCount:
                longestSubArrayCount = count
            i += 1
                
        return longestSubArrayCount
            
    
def countLongestArray(string,index):
    dictionary = {}
    length = len(string)
    i = index
    while i < length and not isPresent(string[i], dictionary):
        dictionary[string[i]] = string[i]
        i += 1
    return i - index
        
def isPresent(key,dictionary):
    if dictionary.get(key) == None:
        return False
    return True