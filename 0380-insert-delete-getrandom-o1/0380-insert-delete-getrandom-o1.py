import random
class RandomizedSet:

    def __init__(self):
        self.t = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.t:
            self.t.add(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        
        if val not in self.t:
            return False
        w = set()
        for i in self.t:
            if i==val:
                continue
            else:
                w.add(i)
        self.t = w
        return True
                
        
        

    def getRandom(self) -> int:
        return random.choice(list(self.t))
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()