# Example Test Cases
testCases = [121, -121, 10]
expectedResults = [True, False, False]


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        for i in range(0, int(len(s)/2+1)):
            if s[i] != s[-i-1]:
                return False
        return True


# Testing
for i in range(0, len(testCases)):
    if Solution.isPalindrome(Solution, testCases[i]) == expectedResults[i]:
        print(f"Test case {i+1} was valid")
    else:
        print(f"Test case {i+1} was INVALID")
