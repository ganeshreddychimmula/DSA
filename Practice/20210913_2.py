'''
Coursera Data Structures
week 1 programming assignment
program 1: Check brackets in the code
'''
from collections import defaultdict
def validate(inp):
    stack = []
    d = defaultdict(str)
    d["]"] = "["
    d["}"] = "{"
    d[")"] = "("
    open = list(d.values())
    close = list(d.keys())
    l = len(inp)
    i = 0
    for i in range(l):
        if inp[i] in open:
            stack.append(i)
        elif inp[i] in close:
            if not stack:
                return i + 1
            else:
                index = stack.pop()
                if d[inp[i]] != inp[index]:
                    return i+1
    if stack:
        return stack[-1] + 1
    return "Success"

inp = list(input().strip())
print(validate(inp))


'''
Input:
{[]}()
Output:
Success

Input:
{[}
Output:
3
'''