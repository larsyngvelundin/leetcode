test_cases = [
    ["ab", "a"],
    ["teststring"],
    ["flower", "flow", "flight"],
    ["dog", "racecar", "car"]
]

expected_results = [
    "a",
    "teststring",
    "fl",
    ""
]


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        shortestString = len(strs[0])
        for string in strs:
            if len(string) < shortestString:
                shortestString = len(string)
        prefix = ""
        for i in range(0, shortestString):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[j-1][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix


# Testing
for i in range(0, len(test_cases)):
    result = Solution.longestCommonPrefix(Solution, test_cases[i])
    if result == expected_results[i]:
        print(f"==Test case {i+1} was valid")
        print(f"✔️  Got '{result}', expected {expected_results[i]}")
    else:
        print(f"==Test case {i+1} was INVALID")
        print(f"❌ Got '{result}', expected {expected_results[i]}")
    #stop = input(f"")
