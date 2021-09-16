'''
Optimum location of point to minimize total distance
https://www.geeksforgeeks.org/optimum-location-point-minimize-total-distance/
'''
from math import sqrt
class Optimum_distance():
    # point object is used to make access easy
    class point:
        def __init__(self,x,y):
            self.x=x
            self.y=y
    # line
    class Line:
        def __init__(self,a,b,c):
            self.a = a
            self.b = b
            self.c = c

    # method to get distance
    # distance from x,y to point p
    def dist(self, x, y, p):
        return sqrt((x-p.x)**2 + (y-p.y)**2)
    #  method to compute total distance which is sum of distances from all points
    # p is array of all points , l is line(a,b,c) , X is x-coordinate
    def totaldist(self,p,n,l,x):
        res = 0
        y = -1*(l.a*x + l.c)/l.b
        for i in range(n):
            res += self.dist(x, y, p[i])
        return res

    #  method to find minimum total distance
    def find_Optimum_cost_untill(self,p,n,l):
        low = -1e6
        high = 1e6
        eps = 1e-6 +1
        # ternary search
        # if we just choose high>=low like binary search
        # then for 1term between high and low it will be infinite loop
        while (high-low)>eps:
            mid1 = low + (high - low)/3
            mid2 = high - (high - low)/3

            # calculating total distance from mid1, mid2 to every point
            dist1 = self.totaldist(p, n, l, mid1)
            dist2 = self.totaldist(p, n, l, mid2)

            if (dist1 < dist2):
                # if mid1 is closet to the point we need
                high = mid2
            else:
                low = mid1
        return self.totaldist(p, n, l, (low+high)/2)

    # main method where we convert array to point object and call above method
    def find_Optimum_cost(self, p, l):
        n=len(p)
        p_arr=[None]*n
        for i in range(n):
            p_obj = self.point(p[i][0],p[i][1])
            p_arr[i] = p_obj
        return self.find_Optimum_cost_untill(p_arr, n, l)



obj = Optimum_distance()
l = obj.Line(1, -1, -3)

p = [[-3, -2], [-1, 0],
     [-1, 2], [1, 2],
     [3, 4]]

print(obj.find_Optimum_cost(p, l))