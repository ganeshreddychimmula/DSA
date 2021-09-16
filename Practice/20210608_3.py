'''
Greedy Techniques to find minimum number of platforms
Asked In:
List of arrival and departure time is given, Find the minimum number of platforms are required for the railway as no train waits
'''


def minimumNumberPlatform(arrival, departure, n):
    max_train = 1
    platform_needed = 0  # waiting or idle trains in station
    i = j = 0
    arrival.sort()
    departure.sort()
    while i < n and j < n:
        if arrival[i] < departure[j]:
            platform_needed += 1
            if platform_needed > max_train:
                max_train = platform_needed
            i += 1
        else:
            platform_needed -= 1
            j += 1

    return max_train


arrival = [100, 140, 150, 200, 215, 400]
departure = [110, 300, 220, 230, 315, 600]
n = len(arrival)

print("Minimum Number Platforms = ", minimumNumberPlatform(arrival, departure, n))