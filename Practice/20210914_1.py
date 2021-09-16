'''
Have the function MostFreeTime(strArr) read the strArr parameter being passed which will represent a full day
 and will be filled with events that span from time X to time Y in the day.
 The format of each event will be hh:mmAM/PM-hh:mmAM/PM.
 For example, strArr may be ["10:00AM-12:30PM","02:00PM-02:45PM","09:10AM-09:50AM"].
 Your program will have to output the longest amount of free time available between the start
 of your first event and the end of your last event in the format: hh:mm.
 The start event should be the earliest event in the day and the latest event should be the latest event in the day.
 The output for the previous input would therefore be 01:30 (with the earliest event in the day
 starting at 09:10AM and the latest event ending at 02:45PM). The input will contain at least 3 events and the events may be out of order.

'''
def caltime(s):
    hr = int(s[:2])
    mn = int(s[3:5])
    if s[5]== "P" and hr != 12:
        hr +=12
    return hr*60 + mn

def longest(arr): # function that calculates the longest leisure
    l = len(arr)
    interval = [] # array to store intervals
    for i in range(l):
        string = arr[i].split("-")
        start = string[0]
        end = string[1]
        interval.append([caltime(start),caltime(end)])
    interval = sorted(interval)
    maxl = -1
    for i in range(1, l):
        if interval[i-1][1] < interval[i][0]:
            maxl = max(interval[i][0] - interval[i-1][1], maxl)
    # print(maxl)
    # print(interval)
    return maxl

inp = ["10:00AM-12:30PM","02:00PM-02:45PM","09:10AM-09:50AM"] # input
print(longest(inp))