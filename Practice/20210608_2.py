'''
Greedy Techniques to find minimum number of platforms
Asked In:
List of arrival and departure time is given, Find the minimum number of platforms are required for the railway as no train waits
'''

def minimumNumberPlatform(arrival, departure, n):
    max_train=1
    w_list=[]
    arrival.sort()
    departure.sort()
    j=0
    i=0
    #traverse through every arrival
    while i<len(arrival):
        #putting arrived trains into waiting list
        w_list.append(arrival[i])
        print(w_list)
        #calculating max number of trains in waiting list
        if len(w_list)>max_train:
            max_train=len(w_list)
        #for everu train in wait list if departure time is less than arrival of next train it departs
        #and it is removed from wit list
        for k in range(len(w_list)):
            if i+1<len(arrival) and departure[j]<=arrival[i+1] :
                del w_list[0]
                j+=1
        #increment to next arrival
        i+=1

    # Practise Yourself :  Write your code Here
    return max_train


arrival = [100, 140, 150, 200, 215, 400]
departure = [110, 300, 220, 230, 315, 600]
n = len(arrival)

print("Minimum Number Platforms = ", minimumNumberPlatform(arrival, departure, n))