test_cases = [
    [3, 1, 2, 4],
    [0]
]

expected_results = [
    [2, 4, 3, 1],
    [0]
]


class Solution:
    def sortArrayByParity(self, nums):
        new_list = []
        for i in range(0, len(nums)):
            if nums[i] % 2 == 0:
                new_list.insert(0, nums[i])
            else:
                new_list.append(nums[i])
        return new_list


# Testing
for i in range(0, len(test_cases)):
    print("==================================")
    result = Solution.sortArrayByParity(
        Solution, test_cases[i])
    if result == expected_results[i]:
        print(f"==Test case {i+1} was valid")
        print(f"✔️  Got '{result}', expected {expected_results[i]}")
    else:
        print(f"==Test case {i+1} was INVALID")
        print(f"❌ Got '{result}', expected {expected_results[i]}")
