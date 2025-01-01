class RangeModule:

    def __init__(self):
        self.left_limit = 1
        self.right_limit = 100

    def addRange(self, left: int, right: int) -> None:
        self.left_limit = left
        self.right_limit = right
        self.interval = []
        for index in range(left, right, 1):
            self.interval.append(index)

    def updateInterval(self, left: int, right: int -> bool):
        self.interval = self.interval[left:self.left_limit] + self.interval[right:self.right_limit]

    def queryRange(self, left: int, right: int) -> bool:
        if left <= self.left_limit and right < self.right_limit:
            return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        if left >= self.left_limit:
            self.left_limit = left
        
        if right < self.right_limit:
            self.right_limit  = right


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)