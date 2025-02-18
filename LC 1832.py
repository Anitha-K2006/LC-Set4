class Solution(object):
    def checkIfPangram(self, sentence):
        check=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
        count=0
        for i in check:
            if i in sentence:
                count+=1
            else:
                break
        return count>=26
solution=Solution()
        
