'''
Example Input 1:
abc*+

Example Output 1:
(a+(b*c))

Example Input 2:
ab+zx+*

Example Output 2:
((a+b)*(z+x))
'''

def normal(leftop, rightop, symbol):
    return "(" + leftop + symbol + rightop +")"

def convert(exp):
    arr = ["*", "+", "-", "/" ]
    arrlist = list(exp)
    l = len(exp)
    i = 0
    while i<len(arrlist):
        if arrlist[i] in arr:
            s = normal(arrlist[i-2],arrlist[i-1],arrlist[i])
            arrlist[i-2] = s
            del arrlist[i-1:i+1]
            i = i-2
        i+=1
    # print(arrlist)

    return arrlist[0]

postex = input()
print(convert(postex))