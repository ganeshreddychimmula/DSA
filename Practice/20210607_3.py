'''
Linear time approach to solve jump game problem
Asked In: AdobeIntuit
You have an array of non-negative integers,you are initially positioned at the first index of the array.Each element
in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index in O(n) Time complexity and O(1) Space Complexity Asked in: Adobe, Intuit
Example:
Input 1:
A = [2,3,1,1,4]
Input 2:
A = [3,2,1,0,4]
Output 1:
2
Explanation 1:
Index 0 -> Index 2 -> Index 4
Output 2:
0
Explanation 2:
There is no possible path to reach the last index return -1
'''


def minJumpsToEnd(num, n):
    # current ladder , number of steps or jumps = num[0]
    #cladder takes input highest steps that can be taken and parses through array untill it becomes 0
    cladder = num[0]
    #while cladder parses array sladder takes the element that offers farthest jump
    # stored ladder for later purpose when cladder becomes 0
    sladder = num[0]
    jump = 1
    for i in range(n):
        #i reached to end of array without exiting means jump successul
        if i == n - 1:
            return jump
        #i increased means one jump happened and avaialable jumps are decreased by one
        cladder -= 1
        sladder -= 1
        #it means no more steps left, means array cnnot be reached in any order
        if cladder == -1:
            return -1
        #highest available ladder are copied into sladder
        if num[i] > sladder:
            sladder = num[i]
        #jump from current ladder to stored ladder that gives higher steps
        if cladder == 0:
            jump += 1
            cladder = sladder
        #if cladder still zero then it means no additional jumps avaialable

    return jump


array1 = [2, 3, 1, 1, 4]
size = len(array1)

# Calling the minJumpsToEnd function
print("Minimum number of jumps to reach end is ", minJumpsToEnd(array1, size))