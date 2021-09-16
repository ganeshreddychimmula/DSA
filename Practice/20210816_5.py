'''
greedy algorithms coursera assignment 5
'''

def minvisits(arr, n):
    arr = sorted(arr)
    # print(arr)
    stack = []
    for i in range(n):
        if i==0 or stack[-1][1] < arr[i][0]:
            stack.append(arr[i])
        else:
            stack[-1] = [max(stack[-1][0], arr[i][0]), min(stack[-1][1], arr[i][1])]
    print(len(stack))
    # print(stack,end="")
    for i in range(len(stack)):
        print(stack[i][1], end=" ")


n = int(input())
intervals = []
for _ in range(n):
    a, b = map(int, input().strip().split())
    intervals.append([a, b])
minvisits(intervals, n)

'''
3
1 3
2 5
3 6
Output:
1
3

4
4 7
1 3
2 5
5 6
Output:
2
3 6
'''