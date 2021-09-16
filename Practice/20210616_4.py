'''
Array puzzle of solving celebrity problem
You are in a party of N people, where only one person is known to everyone.
Such a person may be present at the party, if yes, (s)he doesn’t know anyone at the party.
Your task is to find the celebrity at the party in Time Complexity O(n) Asked in: Google, Flipkart, Amazon, Microsoft
Example:
Input:
matrix = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. matrix[i][j] = 1 means person i knows person j,
otherwise matrix[i][j] = 0 means person i does not know person j.
 The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
'''
MATRIX = [[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0]]
matrix = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]

def knows(a, b):
    return MATRIX[a][b]


# Returns id of celebrity
def findCelebrity(n):
    x = 0
    y = n - 1
    while x < y:
        if knows(x, y) == 1:
            x += 1
        else:
            y -= 1
    for y in range(n):
        if ((y != x) and ((knows(x, y) ==1) or  (knows(y, x))==0 )):
            return -1;

    return x


if __name__ == '__main__':

    n = 4
    idx = findCelebrity(n)

    if (idx == -1):
        print("No celebrity Found")
    else:
        print("Celebrity ID is", idx)