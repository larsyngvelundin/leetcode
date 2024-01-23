test_cases = [
    [1,2,2,4],
    [1,1],
    [3,2,2]
]

expected_results = [
    [2,3],
    [1,2],
    [2,1]
]


class Solution:
    def findErrorNums(self, nums):
        print(f"nums: {nums}")
        n = len(nums)
        print(f"n: {n}")
        s = int((n*(n+1))/2)
        print(f"sum: {s}")
        missing = s - sum(set(nums))
        print(f"missing: {missing}")
        duplicate = sum(nums) - s + missing
        print(f"duplicate: {duplicate}")
        return [duplicate, missing]




# Testing
for i in range(0, len(test_cases)):
    print("==================================")
    result = Solution.findErrorNums(
        Solution, test_cases[i])
    if result == expected_results[i]:
        print(f"==Test case {i+1} was valid")
        print(f"✔️  Got '{result}', expected {expected_results[i]}")
    else:
        print(f"==Test case {i+1} was INVALID")
        print(f"❌ Got '{result}', expected {expected_results[i]}")
