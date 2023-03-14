test_cases = [
    [1, 1, 2],
    [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
    [-1, 0, 0, 0, 0, 3, 3]
]

expected_results = [
    [1, 2],
    [0, 1, 2, 3, 4],
    [-1, 0, 3]
]


class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 1
        while i < len(nums):
            if (nums[i] == nums[i-1]):
                nums.pop(i)
            else:
                i += 1
        return nums


# Testing
for i in range(0, len(test_cases)):
    result = Solution.removeDuplicates(Solution, test_cases[i])
    if result == expected_results[i]:
        print(f"==Test case {i+1} was valid")
        print(f"✔️  Got '{result}', expected {expected_results[i]}")
    else:
        print(f"==Test case {i+1} was INVALID")
        print(f"❌ Got '{result}', expected {expected_results[i]}")
