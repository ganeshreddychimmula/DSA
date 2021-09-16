'''
permutations of a given string without using any predefined libraries
prints duplicates also
'''


# this function is used to convert list to string
def tostring(list):
    return ''.join(list)

# main function that prints all permutations
# a - string
def permute(a, start, end):
    # if the we reach root node then print node
    if start == end:
        print(tostring(a))
    else:
        # for each node put all available values at start
        # for that we have to swap the element at start with itself and every other on it's right
        for i in range(start, end + 1, 1):
            a[start], a[i] = a[i], a[start]
            # fixed till start so go for next index
            permute(a,start+1,end)
            # after completion of all possible values with above fixed subsequence we go back to parent node
            a[start], a[i] = a[i], a[start] #backtrack

string="ABCD"
n=len(string)
a=list(string)
permute(a,0,n-1)