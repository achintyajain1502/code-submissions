class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        r=[]
        for i in points:
            l.append(math.sqrt(pow(i[0],2)+pow(i[1],2)))
        for i in range(k):
            m=l.index(min(l))
            r.append(points[m])
            del l[m]
            del points[m]
        return r
