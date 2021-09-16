'''
https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/approximate/write-a-checker/

'''
'''
4
a 12 c d
b 13 d e
d 12 f k
zz 13 m co
'''
def redundancy(arr,n):
    res=[]
    for i in range(n):
        for j in range(i+1,n):
            if [i,j] in res:
                continue
            else:
                if arr[i][0]==arr[j][0] or arr[i][1]==arr[j][1] or arr[i][2]==arr[j][2] or arr[i][3]==arr[j][3]:
                    res.append([i,j])
                    print("%d %d"%(i+1,j+1))
n=int(input())
arr=[]
for i in range(n):
    t_arr=list(map(str,input().strip().split()))
    arr.append(t_arr)
    arr[i][1]=int(arr[i][1])
#print(arr)
redundancy(arr,n)