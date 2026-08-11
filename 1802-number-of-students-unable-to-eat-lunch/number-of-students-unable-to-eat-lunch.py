class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        i=0
        c=0
        while sandwiches and sandwiches[0] in students:
            if students[i]==sandwiches[i]:
                del students[i]
                del sandwiches[i]
            else:
                k1=[students[0]]
                students=students[1:]+k1
        return len(students)
        