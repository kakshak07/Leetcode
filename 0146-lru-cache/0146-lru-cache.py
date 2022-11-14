from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.dictOrd = OrderedDict()
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self.dictOrd:
            return -1
        # val = self.dictOrd[key]
        rem = self.dictOrd.pop(key)
        self.dictOrd[key] = rem
        return rem
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.dictOrd:
            self.dictOrd.pop(key)
            # self.dictOrd[key] = value
            # return
        else:
            if self.size>0:
                self.size -= 1
            else:
                self.dictOrd.popitem(last=False)
        # self.dictOrd[key] = value
        # t = self.dictOrd.pop(key)
        self.dictOrd[key] = value




# def set(self, key, value):
#     if key in self.dic:    
#         self.dic.pop(key)
#     else:
#         if self.remain > 0:
#             self.remain -= 1  
#         else:  # self.dic is full
#             self.dic.popitem(last=False) 
#     self.dic[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)