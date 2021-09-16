'''
Write a program to reverse an array or string
https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

'''
#swap ith element from start and end.

def reverseWord(s):
    arr=list(s)
    n=len(arr)
    for i in range((n//2)):
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    st="".join(arr)
    return st
s="programtoreverseanarrayorstring"
print(reverseWord(s))