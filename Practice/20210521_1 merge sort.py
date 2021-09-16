'''
merge sort

[8,4,3,12,25,6,13,10]

creating references of array to manipulate divided parts
'''
def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]#0 to mid-1 indexes are only referred
        R=arr[mid:]
        #dividing
        mergesort(L)
        mergesort(R)

        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
            print(arr)

        while i<len (L):
            arr[k]=L[i]
            k+=1
            i+=1

        while j<len(R):
            arr[k]=R[j]
            k+=1
            j+=1







arr=list(map(int,input().strip('[]').split(',')))
mergesort(arr)
print(arr)