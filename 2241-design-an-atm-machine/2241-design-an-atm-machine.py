class ATM(object):

    def __init__(self):
        self.count = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        self.count = [a + b for a, b in zip(self.count, banknotesCount)]
        

    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
        count = [0, 0, 0, 0, 0]
        trans = [20, 50, 100, 200, 500]

        for i in range(len(self.count) - 1, -1, -1):
            total = min(self.count[i], amount // trans[i])
            amount -= total * trans[i]
            count[i] += total

        if amount != 0:
            return [-1]

        self.deposit(list(map(lambda v: -v, count)))
        return count


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)