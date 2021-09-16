'''
Print all subsequences of a given string
https://www.geeksforgeeks.org/print-subsequences-string/
'''
def printSubsequence(input, output):
    # Base Case
    # if the input is empty print the output string
    if len(input) == 0:
        print(output, end=' ')
        return
    # output is passed with including the 1st character of input string
    printSubsequence(input[1:], output + input[0])

    # output is passed without including the 1st character of input string
    printSubsequence(input[1:], output)

# output is set to null before passing in
# as a parameter
output = ""
input = "abcd"

printSubsequence(input, output)


