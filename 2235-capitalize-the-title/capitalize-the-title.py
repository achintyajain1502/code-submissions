class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        title=title.split(" ")
        l=[]
        for i in title:
            # print i
            if len(i)<=2:
                # print True
                l.append(i.lower())
                # print i
            else:
                # print False
                l.append(i.title())
        title=""
        for i in l:
            title=title +" "+ i
        title=title.lstrip()
        return title
