from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.k=deque()
        
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.k.append(t)
        while self.k[0]<t-3000:
            self.k.popleft()
        return len(self.k)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)