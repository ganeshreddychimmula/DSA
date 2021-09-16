'''
Rectangle Overlap problem
Asked In: GoldmanSachsExpediaOLA
Rectangle that is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinates of its top-left corner,
and (x2, y2) is the coordinates of its bottam-right corner. Now two rectangles overlap if the area of their intersection is positive.
Two rectangles that only touch at the corner or edges do not overlap.
Check in O(1) Time complexity and O(1) Space complexity that both rectangle overlap or not
Asked in: GoldmanSachs, Expedia, OLA
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Returns true if two rectangles(S, P) and (S1, P1) overlap



def checkOverlapRectangle(S, P, S1, P1):
    #S.x>=P1.x -> if true implies that second rectangle is on left  to first rectangle and non-overlapping
    #P.x<=S1.x -> if true implies that second rectangle is on right to first rectangle and non-overlapping
    if S.x>=P1.x or P.x<=S1.x:
        return False
    # S.y1<=P1.y -> if true implies that second rectangle is above first rectangle and non-overlapping
    # P.y>=S1.y -> if true implies that second rectangle is below first rectangle and non-overlapping
    if S.y<=P1.y or P.y>=S1.y:
        return False
    return True


if __name__ == "__main__":
    S = Point(0, 10)
    P = Point(10, 0)
    S1 = Point(5, 5)
    P1 = Point(15, 0)

    if (checkOverlapRectangle(S, P, S1, P1)):
        print("Rectangles Overlap")
    else:
        print("Rectangles Don't Overlap")