class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        sortedBoat = people.sort(reverse=True)
        
        i = 0
        j = len(people) - 1
        counter = 0
        while(i<=j):
            if people[i] + people[j] <= limit: 
                j -= 1
            i += 1
        return i
                
        