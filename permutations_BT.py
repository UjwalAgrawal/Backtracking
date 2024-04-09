from typing import List

def permutations(nums: List[int]) -> List[List[int]]:
    l = [] # start with an empty list
    def solve(start):
        if(start == len(nums) - 1): # till we reach last element and have no more elements to swap with
            l.append(nums.copy()) # Append a copy of nums to l
            return
        s = set()
        for i in range(start, len(nums)):
            if(nums[i] not in s):
                s.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                solve(start+1)
                nums[start], nums[i] = nums[i], nums[start]
           
    solve(0)
    return l

nums = [1,2,3]
result = permutations(nums)
print(result)