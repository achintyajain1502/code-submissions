class MinStack(object):

    def __init__(self):
        self.l=[]
        self.ml=[]

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.l.append(value)
        if not self.ml:
            self.ml.append(value)
        else:
            self.ml.append(min(self.ml[-1],value))
        

    def pop(self):
        """
        :rtype: None
        """
        del self.l[-1]
        del self.ml[-1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.l[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.ml[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()