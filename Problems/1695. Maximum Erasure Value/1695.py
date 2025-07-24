from examples import test_cases, expected_results


class Solution:
    def maximumUniqueSubarrayNew(self, nums: list[int]) -> int:
        current_sub = []
        left_index = 0
        max_sum = 0
        current_sum = 0
        for right_index, value in enumerate(nums):
            while value in current_sub:
                current_sum -= current_sub[0]
                current_sub.pop(0)
            current_sub.append(value)
            current_sum += value
            max_sum = max(current_sum, max_sum)
        return max_sum

    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        self.max = 0
        for index, value in enumerate(nums):
            # print(f"Current max: {self.max}")
            # print(f"Checking nums[{index}] ({value})")
            # print(f"index: {index}")
            # print(f"index+1: {index+1}")
            # print(f"nums: {nums}")
            # print(f"nums[index+1:]: {nums[index+1:]}")
            # print(
            # f"nums[index+1:].index(value): {nums[index+1:].index(value)}")
            # print(f"full sublist: {nums[index:]}")
            # temp_s =
            found_duplicate = 0
            for subindex, subvalue in enumerate(nums[index:]):
                temp_sublist = nums[index:index+subindex]
                # print(temp_sublist)
                if subvalue in temp_sublist:
                    found_duplicate = 1
                    self.max = self.updateMax(
                        self, self.max, sum(temp_sublist))
                    break
            if not found_duplicate:
                self.max = self.updateMax(self, self.max, sum(nums[index:]))

            # try:
            #     next_occurrence = nums[index:].index(value, 2)
            #     sublist_sum = sum(nums[index:next_occurrence])
            #     max = self.updateMax(self, max, sublist_sum)
            # except Exception:
            #     next_occurrence = len(nums)
            #     sublist_sum = sum(nums[index:next_occurrence])
            #     max = self.updateMax(self, max, sublist_sum)
            #     return max
            # print(
            #     f"value to value: {nums[index:next_occurrence]}")

            # for subindex, subvalue in enumerate(nums[index:nums[index+1:].index(value)]):
            #     print(f"    Checking nums[{subindex}] ({subvalue})")
        return self.max

    def updateMax(self, max: int, new_value: int) -> int:
        # print(f"=== Updating max({max}) with new_value({new_value})")
        if new_value > max:
            return new_value
        return max


# Testing
for i in range(0, len(test_cases)):
    result = Solution.maximumUniqueSubarrayNew(Solution, test_cases[i])
    # result = Solution.maximumUniqueSubarray(Solution, test_cases[i])
    if result == expected_results[i]:
        print(f"==Test case {i+1} was valid")
        print(f"✔️  Got '{result}', expected {expected_results[i]}")
    else:
        print(f"==Test case {i+1} was INVALID")
        print(f"❌ Got '{result}', expected {expected_results[i]}")
