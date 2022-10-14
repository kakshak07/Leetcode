class FindSumPairs:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.dict1 = Counter(nums2)

    def add(self, index, val):
        self.dict1[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.dict1[self.nums2[index]] += 1

    def count(self, tot):
        total = 0

        for i in self.nums1:
            total += self.dict1[tot-i]

        return total


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)