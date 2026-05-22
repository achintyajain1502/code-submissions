class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        l=title.split(" ")
        for i in range(len(l)):
            if(len(l[i])==1 or len(l[i])==2):
                l[i]=l[i].lower()
            else:
                l[i]=l[i].lower().title()
        title=" ".join(l)
        return(title)