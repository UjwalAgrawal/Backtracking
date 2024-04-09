# all permutations without backtracking. need of backtracking arises because in each call we are creating 
# a new copy of input, which can take more memory.

from typing import List

def permutations(nums: List[int]) -> List[List[int]]:
    l = [] # start with an empty list
    def solve(input, output):
        if(len(input)==0): #since in each call the input size is decreasing
            l.append(output)
            return
        s = set()
        for i in range(len(input)):
            if(input[i] not in s):
                newInput = input[:i] + input[i+1:] #take the i'th element out and put it in the output list
                newOutput = output + [input[i]]
                s.add(input[i]) #keeping a memory of used characters / elements of the list
                solve(newInput, newOutput)
    solve(nums, [])
    return l

nums = [1,2,3]
result = permutations(nums)
print(result)