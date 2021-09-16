'''
Distribute Candy
Asked In: FlipkartAmazonMicrosoft
There are N children standing in a line with some rating value.
You want to distribute a minimum number of candies to these children such that: Each child must have at least one candy.
The children with higher ratings will have more candies than their neighbors.
You need to write a program to calculate the minimum candies you must give.
'''
'''
condition was that any element that has geater rating tha it's meighbour should have greater candiies than neighbour
means element having rating greater than left or right or both must have rating greater than left or right or both neighbours
'''
class Main:
    def candy(self, ratings):
        if (ratings == None or len(ratings) == 0):
            return 0
        #satisfying the condition that each children should be provided atleast one choclate
        left = [1] * len(ratings)
        right = [1] * len(ratings)
        result_array=[]
        result = 0
        #we divide problem into 2 sub problems
        #each element greater than it's left element should have 1 more candies
        for i in range(1, len(ratings), 1):
            if (ratings[i] > ratings[i - 1]):
                left[i] = left[i - 1] + 1

        # each element greater than it's right element should have 1 more candies
        for i in range(len(ratings) - 2, -1, -1):
            cur = 1
            if (ratings[i] > ratings[i + 1]):
                right[i] = right[i + 1] + 1
        #in summary number of candies greater than of both of neighbours is considered
        for i in range(0, len(ratings), 1):
            result += max(right[i], left[i])
            result_array.append(max(right[i], left[i]))
        print(result_array)
        return result


m = Main()
ratings = [1, 5, 2, 1]
ratings=[12,4,3,11,34,34,1,67]
result = m.candy(ratings)
print(result)