'''
Longest Palindrome in a String
https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1#
'''
class Solution:
    def ispalindrome(self,arr,x,y):
        arr1=arr[x:((x+y)//2) + 1] if (y-x+1)%2==0 else arr[x:(x+y)//2]
        arr2=arr[y:(x+y)//2 : -1]
        #print(x,y,arr1,arr2,(x+y)//2)
        if arr1==arr2:
            return True
        else:
            return False
    def longestPalin(self, S):
        n=len(S)
        if not S:
            return -1
        if n==1:
            return S
        S=list(S)
        maxlen=0
        start=end=-1
        '''
        take 2 pointers , pointer one traverses from 0 to n-1  in front one
        from back check for palindrome possibility from  
        '''
        for i in range(n-1):
            for j in range(n-1,i,-1):
                if self.ispalindrome(S,i,j) and j-i+1>maxlen:
                    start=i
                    end=j
                    maxlen=j-i+1
        #print(start,end)
        if maxlen==0:
            return "".join(S[0])
        result="".join(S[start:end+1])
        return result
obj = Solution()
# S="abc"
S="aaaabbaa"
print(obj.longestPalin(S))