test_cases = [[2, 2, 1], [4, 1, 2, 1, 2], [1]]

expected_results = [1, 4, 1]


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for _, value in enumerate(nums):
            result = result ^ value
        return result


for i in range(0, len(test_cases)):
    print("==================================")
    result: int = Solution.singleNumber(Solution, test_cases[i])
    if result == expected_results[i]:
        print(f"==Test case {i + 1} was valid")
        print(f"✔️  Got '{result}', expected {expected_results[i]}")
    else:
        print(f"==Test case {i + 1} was INVALID")
        print(f"❌ Got '{result}', expected {expected_results[i]}")
