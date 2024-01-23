test_cases = [
    "Let's take LeetCode contest",
    "God Ding"
]

expected_results = [
    "s'teL ekat edoCteeL tsetnoc",
    "doG gniD"
]


class Solution:
    def reverseWords(self, s):
        list = s.split(" ")
        new_list = []
        for word in list:
            new_word = ""
            for letter in word:
                new_word = letter + new_word
            new_list.append(new_word)
        new_string = " ".join(new_list)
        return new_string


        # Testing
for i in range(0, len(test_cases)):
    print("==================================")
    result = Solution.reverseWords(
        Solution, test_cases[i])
    if result == expected_results[i]:
        print(f"==Test case {i+1} was valid")
        print(f"✔️  Got '{result}', expected '{expected_results[i]}'")
    else:
        print(f"==Test case {i+1} was INVALID")
        print(f"❌ Got '{result}', expected '{expected_results[i]}'")
