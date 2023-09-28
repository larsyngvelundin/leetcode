test_cases = [
    [1, 2, 3],
    [4, 3, 2, 1],
    [9],
    [5, 9, 9],
    [9, 9],
    [9, 8, 9]
]

expected_results = [
    [1, 2, 4],
    [4, 3, 2, 2],
    [1, 0],
    [6, 0, 0],
    [1, 0, 0],
    [9, 9, 0]
]


class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits


        # Testing
for i in range(0, len(test_cases)):
    print("==================================")
    result = Solution.plusOne(
        Solution, test_cases[i])
    if result == expected_results[i]:
        print(f"==Test case {i+1} was valid")
        print(f"✔️  Got '{result}', expected {expected_results[i]}")
    else:
        print(f"==Test case {i+1} was INVALID")
        print(f"❌ Got '{result}', expected {expected_results[i]}")
