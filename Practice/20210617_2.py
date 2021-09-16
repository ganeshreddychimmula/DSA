'''
Minimize the Heights II
https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1#

'''


def getMinDiff(arr, n, k):
    v = []
    taken = [0] * n # is used to keep track of elements if already used or not
    #append each element with k subtract if it is non-negative and addition of k along with index number
    for i in range(n):
        if arr[i] - k >= 0:
            v.append([arr[i] - k, i])
        v.append([arr[i] + k, i])

    v.sort()
    #print(v)
    elements_in_range = 0
    left = 0
    right = 0

    while elements_in_range < n and right < len(v):
        #if the element is not taken incremnet elements in range
        if taken[v[right][1]] == 0:
            elements_in_range += 1
        #update taken value of the index
        taken[v[right][1]] += 1
        right += 1#move one step right

    ans = v[right - 1][0] - v[left][0]

    while right < len(v):

        if (taken[v[left][1]] == 1):
            elements_in_range -= 1

        taken[v[left][1]] -= 1
        left += 1

        while elements_in_range < n and right < len(v):
            if taken[v[right][1]] == 0:
                elements_in_range += 1

            taken[v[right][1]] += 1
            right += 1

        if (elements_in_range == n):
            ans = min(ans, v[right - 1][0] - v[left][0])
        else:
            break

    return ans


arr=[3, 9, 12, 16, 20]
print(getMinDiff(arr,len(arr),3))