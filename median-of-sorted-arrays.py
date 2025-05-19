class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        def merge_sort(list1, list2):
            sorted_list = []
            count1 = 0
            count2 = 0
            while count1 < len(list1) and count2 < len(list2):
                if list1[count1] <= list2[count2]:
                    sorted_list.append(list1[count1])
                    count1 += 1
                else:
                    sorted_list.append(list2[count2])
                    count2 += 1
            while count1 < len(list1):
                sorted_list.append(list1[count1])
                count1 += 1
            while count2 < len(list2):
                sorted_list.append(list2[count2])
                count2 += 1
            return sorted_list
        sorted_list = merge_sort(nums1, nums2)
        if len(sorted_list) % 2 == 0:
            mid_index = len(sorted_list) / 2
            med =float((sorted_list[mid_index -1] + sorted_list[mid_index])) / 2
        else:
            mid_index = len(sorted_list) // 2
            med = sorted_list[mid_index]
        return med