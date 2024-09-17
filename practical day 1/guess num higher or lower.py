
def guess(num: int) -> int:
    picked_number = 6  
    if num < picked_number:
        return 1
    elif num > picked_number:
        return -1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            
            if result == 0:
                return mid 
            elif result == -1:
                right = mid - 1 
            else:
                left = mid + 1  
        return -1  
