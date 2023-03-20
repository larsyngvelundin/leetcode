test_cases = [
    [[3, 2, 2, 3], 3],
    [[0, 1, 2, 2, 3, 0, 4, 2], 2]
]

expected_results = [
    2, 5
]


class Solution:
    def removeElement(self, nums, val) -> int:
        i = 0
        while i < len(nums):
            if (nums[i] == val):
                nums.pop(i)
            else:
                i += 1
        return len(nums)


# Testing
for i in range(0, len(test_cases)):
    result = Solution.removeElement(
        Solution, test_cases[i][0], test_cases[i][1])
    if result == expected_results[i]:
        print(f"==Test case {i+1} was valid")
        print(f"✔️  Got '{result}', expected {expected_results[i]}")
    else:
        print(f"==Test case {i+1} was INVALID")
        print(f"❌ Got '{result}', expected {expected_results[i]}")
