import time

from tests import test_cases, expected_results


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # print("")
        # print("")
        # print("#####################")
        # print("New test case")
        # print("#####################")
        index1 = 0
        index2 = 0
        max1 = len(nums1)
        max2 = len(nums2)
        result_list = []

        def add_remaining(nums, index):
            while index < len(nums):
                result_list.append(nums[index])
                index += 1
        while index1 is not max1 and index2 is not max2:
            print("#####################")
            print("Start of loop")
            print(f"Result: {result_list}")
            print(f"This loop should happen? {index1 is not max1}")
            print(f"Index 1: {index1}  Max: {max1}")
            print(f"Index 2: {index2}  Max: {max2}")
            print(f"Comparing 1({nums1[index1]}) and 2({nums2[index2]})")
            if nums1[index1] > nums2[index2]:
                result_list.append(nums2[index2])
                index2 += 1
            else:
                result_list.append(nums1[index1])
                index1 += 1
            print(f"Index 1: {index1}")
            index1 += 1
        print("#####################")
        print("Ending first loop")
        print(f"Index 1: {index1}  Max: {max1}")
        print(f"Index 2: {index2}  Max: {max2}")
        if index1 is not max1:
            print("Adding from nums1")
            add_remaining(nums1, index1)
        if index2 is not max2:
            print("Adding from nums2")
            add_remaining(nums2, index2)
        print(f"Final result list: {result_list}")

        if len(result_list) % 2 is 0:
            subtotal = result_list[int(
                len(result_list)/2)] + result_list[int(len(result_list)/2)-1]
            return subtotal / 2
        else:
            return result_list[int(len(result_list)/2)]

        # Testing
for i in range(0, len(test_cases)):
    start_time = time.time()
    result = Solution.findMedianSortedArrays(
        Solution, test_cases[i][0], test_cases[i][1])
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "milliseconds")
    if result == expected_results[i]:
        print(f"==Test case {i+1} was valid")
        print(f"✔️  Got '{result}', expected {expected_results[i]}")
    else:
        print(f"==Test case {i+1} was INVALID")
        print(f"❌ Got '{result}', expected {expected_results[i]}")
