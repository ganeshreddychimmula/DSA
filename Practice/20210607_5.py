
# Given number as int array, this function finds the
# greatest number and returns the number as integer
def findNextNumber(array, n):
    i = n - 1
    left = 0
    immright = 0
    parse = 1
    #traversing left from rightmost until we find an element smaller than its previous element
    while i > 0 and parse == 1:
        if array[i] > array[i - 1]:
            # print(array[i],array[i-1])
            # array[i],array[i-1]=array[i-1],array[i]
            parse = 0
        i -= 1
    immright = i + 1
    # print(i)
    #finding smallest number greater than i
    for j in range(i, n):
        if array[j] > array[i] and array[j] < array[immright]:
            immright = js
    # print(i,immright)
    array[i], array[immright] = array[immright], array[i]
    stri=''.join(map(str,array))
    print("immediate greater number with same digits is ",stri)


digits = "218765"

number = list(map(int, digits))
findNextNumber(number, len(digits))
