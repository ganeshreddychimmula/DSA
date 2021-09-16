'''
A Program to check if strings are rotations of each other or not
https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/
'''
def isrotated(s1,s2):
    n=len(s1)
    temp=s1+s1
    for i in range(n):
        if temp[i:i+n]==s2:
            print(i,temp[i])
            return True
    return False



str1 = "ABACD"
str2 = "CDABA"
print(isrotated(str1,str2))