'''
Common elements
https://practice.geeksforgeeks.org/problems/common-elements1132/1
'''
#User function Template for python3
from collections import defaultdict
class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        d1=defaultdict(int)
        d2=defaultdict(int)
        d3=defaultdict(int)
        #here we are not making use of fact that they are sorted
        #putting each element in dictionary with value 1 such that elemented cannot be repeated
        for i in A:
            d1[i]=1
        for i in B:
            d2[i]=1
        for i in C:
            d3[i]=1
        #print(d1,d2,d3)
        #beacuse if it is common it should be in all arrays
        common=[]
        for i in A:
            if  d1[i]==1 and d2[i]==1 and d3[i]==1 :
                if len(common)==0:#for 1st common  element
                    common.append(i)
                #as array is sorted if common element repeats then we can simply find by commparing
                #with last element in common
                elif i!=common[-1]:
                    common.append(i)
        return common

A=[1, 5, 10, 20, 40, 80]
B=[6, 7, 20, 80, 100]
C=[3, 4, 15, 20, 30, 70, 80, 120]
obj=Solution()
print(obj.commonElements(A,B,C,len(A),len(B),len(C)))
