'''
Lb List-Palindromic Array
https://practice.geeksforgeeks.org/problems/palindromic-array-1587115620/1#
'''
def PalinArray(arr ,n):
    for i in range(n):
        temp=arr[i]
        rev=0
        while arr[i]>=1:
            rev=rev*10+arr[i]%10
            arr[i]=arr[i]//10
        if temp!=rev:
            return False

    return True