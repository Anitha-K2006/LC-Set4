class Solution(object):
    def mostWordsFound(self, sentences):
        count=[]
        for i in sentences:
            x=len(i.split())
            count.append(x)
        t=max(count)
        return t
solution=Solution()
