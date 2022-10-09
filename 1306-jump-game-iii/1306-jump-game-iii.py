class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        def recurse(position, set_numbers):
            
            if position in set_numbers:
                return False
            
            set_numbers.add(position)
            
            if position<0 or position >=len(arr):
                return False
            
            if arr[position] == 0:
                return True
            
            return( recurse(arr[position]+position,set_numbers) or recurse(position-arr[position],set_numbers))
        
        return(recurse(start, set()))
            
        