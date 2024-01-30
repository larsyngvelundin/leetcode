test_cases = [
    19,
    2
]

expected_results = [
    True,
    False
]


class Solution:
    def isHappy(self, n: int) -> bool:
        past_nums = [n]
        still_looking = True
        while still_looking:
            n_str = str(n)
            new_n = 0
            for c in n_str:
                n_int = int(c)
                n_int = n_int * n_int
                print(n_int)
                new_n += n_int
            n = new_n
            still_looking = False
        return True


        # Testing
for i in range(0, len(test_cases)):
    print("==================================")
    result = Solution.isHappy(
        Solution, test_cases[i])
    if result == expected_results[i]:
        print(f"==Test case {i+1} was valid")
        print(f"✔️  Got '{result}', expected {expected_results[i]}")
    else:
        print(f"==Test case {i+1} was INVALID")
        print(f"❌ Got '{result}', expected {expected_results[i]}")
