'''
38. Count and Say
https://leetcode.com/problems/count-and-say/submissions/
'''
class Solution:
    def countAndSay(self, n):
        say=[]
        temp=[]
        if n == 1 :
            return "1"
        if n == 2 :
            return "11"
        say=[1,1]
        # as we already managed first t0 we traverse for n-2 times
        for i in range(0,n-2):
            temp=say.copy()
            say=[]
            j=1
            count=1
            while j<len(temp):
                if temp[j]==temp[j-1]:
                    count+=1
                    j+=1
                else:
                    say.append(count)
                    say.append(temp[j-1])
                    count=1
                    j+=1
            #for last element
            say.append(count)
            say.append(temp[j-1])
            #print(say)
        say="".join(list(map(str,say)))
        return say

obj=Solution()
print(obj.countAndSay(4))