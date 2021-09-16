'''
logic mojo arrays
Segregation logic to Sort an array of 0's, 1's and 2's
Array consist of only 0's, 1's and 2's. Write an algorithm to sort  this array in O(n) time complexity and O(1) Space complexity with only one traversal Asked in : : Amazon, Microsoft, Adobe, WalmartLabs

Example:

Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]
Hint1 : You are not suppose to use any extra space
Hint2 : You need change the same array with single traversal with O(n) time complexity
'''
# putting all o's in array before i
# putting all 2's in array after j
def sort(array, end):
     i=0
     mid=0
     j=end
     while mid<=j:#because after j therre wold be only 2's
         #neglect 1's
         if array[mid]==1:
             mid+=1
         #if o is encountered swap with i and increment both beacuase the value that comes will be 1
         elif array[mid]==0:
             array[i],array[mid]=array[mid],array[i]
             i+=1
             mid += 1
         #swap with j and decrement only j because swapped value might be 0 or 1
         elif array[mid]==2:
             array[j], array[mid] = array[mid], array[j]
             j-=1
         #print(array,i,mid,j)
     return array




if __name__ == '__main__':
    array = [2, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    sort(array, len(array) - 1)
    print(array)