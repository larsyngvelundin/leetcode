test_cases = [
    "Hello World",
    "   fly me   to   the moon  ",
    "luffy is still joyboy"
]

expected_results = [
    5,
    4,
    6
]


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        while (s[len(s)-1] == " "):
            s = s[:-1]
        last_word = s.split(" ")[len(s.split(" "))-1]
        return len(last_word)

        # Testing
for i in range(0, len(test_cases)):
    result = Solution.lengthOfLastWord(
        Solution, test_cases[i])
    if result == expected_results[i]:
        print(f"==Test case {i+1} was valid")
        print(f"✔️  Got '{result}', expected {expected_results[i]}")
    else:
        print(f"==Test case {i+1} was INVALID")
        print(f"❌ Got '{result}', expected {expected_results[i]}")
