test_cases = [
    [[1, 3, 5, 6], 5],
    [[1, 3, 5, 6], 2],
    [[1, 3, 5, 6], 7]
]

expected_results = [
    2,
    1,
    4
]


class Solution:
    def searchInsert(self, nums, target) -> int:
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)

        # Testing
for i in range(0, len(test_cases)):
    result = Solution.searchInsert(
        Solution, test_cases[i][0], test_cases[i][1])
    if result == expected_results[i]:
        print(f"==Test case {i+1} was valid")
        print(f"✔️  Got '{result}', expected {expected_results[i]}")
    else:
        print(f"==Test case {i+1} was INVALID")
        print(f"❌ Got '{result}', expected {expected_results[i]}")
