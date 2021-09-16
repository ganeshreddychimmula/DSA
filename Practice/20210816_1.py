'''
greedy algorithms coursera assignment 1
'''
n=0
V = int(input())
n += V//10
n += (V%10)//5
n += (V%10)%5
print(n)