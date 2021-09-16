'''
print all subsequences of a given string
https://www.geeksforgeeks.org/print-all-subsequences-of-a-string-in-python/#:~:text=Given%20a%20string%2C%20we%20have,string%20without%20changing%20its%20order.
'''
import itertools


def sub_sequences(s):
    combs=[]
    # print subsequences of each length l
    for l in range(1,len(s)+1):
        combs.append(list(itertools.combinations(s,l)))
    for c in combs:
        for t in c:
            print("".join(t), end=' ')


sub_sequences("abcd")
