test_cases = [
    "(([]){})",
    "(){}}{",
    "([)]",
    "{[]}",
    "()",
    "()[]{}",
    "()[{}",
    "(]"
]

expected_results = [
    True,
    False,
    False,
    True,
    True,
    True,
    False,
    False
]


class Solution:
    pairs = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    reversed_pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    loops = 0

    def count_pairs(self, sub):
        for start in self.pairs:
            if sub.count(start) != sub.count(self.pairs[start]):
                return False
        return True

    def isValid(self, s: str) -> bool:
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
        if len(s) == 0:
            return True
        return False

        # # start_par = s.count("(")
        # if self.count_pairs(self, s) == False:
        #     # print("Lost here")
        #     return False

        # for i in range(0, len(s)):
        #     print(f"Checking index {i}")
        #     print(f"Char: {s[i]}")
        #     if s[i] in self.pairs.keys():
        #         if self.count_pairs(self, s[i+1:s.find(self.pairs[s[i]])]) == False:
        #             # print(s[i:s.find(self.pairs[s[i]])])
        #             # print("Lost in the loop")
        #             return False
        #         elif s.find(self.pairs[s[i]]) < i:
        #             return False

        # return True
        # # print(start_par)
        # # for i in reversed(range(0, len(s) - 1)):
        # #     self.loops += 1
        # #     if s[i] in self.reversed_pairs.keys():
        # #         for j in reversed(range(0, i-1)):
        # #             if s[j] == self.reversed_pairs[i]:
        # #                 s[i].
        # #     #and self.reversed_pairs[s[i]] != s[i + 1]:
        # #     else:
        # #         return False


# Testing
for i in range(0, len(test_cases)):
    print("")
    print(f"###Starting case {i+1}")
    result = Solution.isValid(Solution, test_cases[i])
    if result == expected_results[i]:
        print(f"==Test case {i+1} was valid")
        print(f"✔️  Got '{result}', expected {expected_results[i]}")
    else:
        print(f"==Test case {i+1} was INVALID")
        print(f"❌ Got '{result}', expected {expected_results[i]}")
    stop = input(f"")


print(f"Loops{Solution.loops}")
