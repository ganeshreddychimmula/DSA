import sys


class Solution:
    # mergesort merge operation until (n+m)/2
    def findMedianSortedArrays(self, nums1, nums2):
        # keeping sure that nums2 len stays bigger
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        x = len(nums1)
        y = len(nums2)
        low = 0
        high = x

        while low <= high:
            partnums1 = (low + high) // 2  # partition in arr1
            partnums2 = ((x + y + 1) // 2) - partnums1  # partition in arr2
            # print(partnums1,partnums2)
            # calcualting leftmaxnusm1
            leftmaxnums1 = -sys.maxsize if partnums1 == 0 else nums1[partnums1 - 1]
            # calculating rightminnums1
            rightminnums1 = sys.maxsize if partnums1 == x else nums1[partnums1]
            # calcualting leftmaxnusm2
            leftmaxnums2 = -sys.maxsize if partnums2==0 else nums2[partnums2-1]
            # calculating rightminnums2
            rightminnums2 = sys.maxsize if partnums2 == y else nums2[partnums2]
            # below condition is partition is done rightly
            if leftmaxnums1 <= rightminnums2 and leftmaxnums2 <= rightminnums1:
                # if partition done right
                if (x + y) % 2 == 0:
                    result = max(leftmaxnums1, leftmaxnums2) + min(rightminnums1, rightminnums2)
                    # print(max(leftmaxnums1, leftmaxnums2),min(rightminnums1, rightminnums2),leftmaxnums1, leftmaxnums2,rightminnums1, rightminnums2)
                    return result / 2
                else:
                    result = max(leftmaxnums1, leftmaxnums2)
                    return result
            elif leftmaxnums1 > rightminnums2:
                high = partnums1 - 1
            else:
                low = partnums1 + 1


obj = Solution()
arr1 = [1, 3, 4, 7, 10, 12]
arr2 = [2, 3, 6, 15]
# arr1 = [0, 0]
# arr2 = [0, 0]
print(obj.findMedianSortedArrays(arr1, arr2))