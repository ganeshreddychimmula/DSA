def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def sort(a):
    i=0
    while i<len(a)-1:
        if a[i]>a[i+1]:
            swap(a,i,i+1)
        print(a)
        i+=1
    array=a[:]


array = [2, 1, 1 , 0, 1, 2, 1, 2, 0, 0, 0, 1]
sort(array)
print(array)




