test_cases = [
    ["sadbutsad", "sad"],
    ["leetcode", "leeto"]
]

expected_results = [
    0,
    -1
]


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


# Testing
for i in range(0, len(test_cases)):
    result = Solution.strStr(
        Solution, test_cases[i][0], test_cases[i][1])
    if result == expected_results[i]:
        print(f"==Test case {i+1} was valid")
        print(f"✔️  Got '{result}', expected {expected_results[i]}")
    else:
        print(f"==Test case {i+1} was INVALID")
        print(f"❌ Got '{result}', expected {expected_results[i]}")
