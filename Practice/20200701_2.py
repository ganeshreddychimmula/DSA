'''
Check if the given string is shuffled substring of another string
https://www.geeksforgeeks.org/check-if-the-given-string-is-shuffled-substring-of-another-string/
'''
def isShuffledSubstring(str1,str2):
    str1,str2=list(str1),list(str2)
    arr1=[0]*256 #for hashing
    arr2=[0]*256
    # print(arr2)
    n1,n2=len(str1),len(str2)
    if n1 > n2 :
        return "NO"
    for i in range(n1):
        #try :
        arr1[ord(str1[i])] += 1
        arr2[ord(str2[i])] += 1
        #except :
        #print(i)

    if arr1==arr2:
        print(arr1,arr2)
        return "YES"
    for i in range(1,n2-n1+1):
        #delete starting elemnt of previous window
        arr2[ord(str2[i-1])] -= 1
        #add last element of current window
        arr2[ord(str2[i+n1-1])] += 1
        if arr1 == arr2:
            print(arr1)
            print(arr2)
            return "YES"
    return "NO"
    pass


str1 = 'onetwofour'
str2 = 'hellofourtwooneworld'
print(isShuffledSubstring(str1,str2))