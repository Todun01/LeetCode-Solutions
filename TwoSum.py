class Solution(object):
    def twoSum(self, nums, target):
        output = []
        isZero = False
        mixedSigns = False
        
        for num in nums:
            if target > 0 and num < 0:
                mixedSigns = True
        # if target is zero
        if target == 0:
            for num in nums:
                if num == 0:
                    isZero = True
            if isZero:
                first_index = nums.index(0)
                for n in range(first_index + 1, len(nums)):
                    if nums[n] == 0:
                        second_index = n
                output = [first_index, second_index]
        # if target is negative
        if target < 0:
            for num in nums:
                if target < num:
                    first_num = num
                    second_num = target - first_num
                    if second_num == first_num:
                        for num in range(nums.index(first_num) + 1, len(nums)):
                            if nums[num] == second_num and len(output) < 2:
                                output.append(nums.index(first_num))
                                output.append(num)
                    else:
                        if second_num in nums and len(output) < 2:
                            output.append(nums.index(first_num))
                            output.append(nums.index(second_num))
        # if target is positive
        for num in nums:
            if target > num:
                first_num = num
                second_num = target - first_num
                if second_num == first_num:
                    for num in range(nums.index(first_num) + 1, len(nums)):
                        if nums[num] == second_num and len(output) < 2:
                            output.append(nums.index(first_num))
                            output.append(num)
                else:
                    if second_num in nums and len(output) < 2:
                        output.append(nums.index(first_num))
                        output.append(nums.index(second_num))
                                            
        return output
        