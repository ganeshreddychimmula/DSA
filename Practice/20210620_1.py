'''
Factorials of large numbers
https://practice.geeksforgeeks.org/problems/factorials-of-large-numbers2508/1#
Complete the function factorial() that takes integer N as input parameter and
 returns a list of integers denoting the digits that make up the factorial of N.
'''
class Solution:
    def factorial(self, N):
        prod=1
        for i in range(N):
            prod*=(i+1)
        arr=[]
        while prod>=1:
            temp=prod%10
            arr.insert(0,temp)
            prod=prod//10
        return arr

obj=Solution()
result=obj.factorial(5)
str="".join(map(str,result))
print(str)