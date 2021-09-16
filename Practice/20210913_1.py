'''
This is a (rule (with a lot of wiggle room. An entire sentence in) parentheses is) often acceptable without an enclosed period, 11
'''

inp, index = map(str, input().split(","))
index = int(index)
inp = list(inp)
stack = []

for i in range(len(inp)):
    if inp[i] == "(":
        stack.append(i)
    elif inp[i] == ")":
        ind = stack.pop()
        if ind == index - 1:
            print(i)
            break
    # print(stack)