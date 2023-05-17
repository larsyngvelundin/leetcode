# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

test_cases = [    
    ListNode(5, ListNode(4, ListNode(2, ListNode(1, None)))),
    ListNode(4, ListNode(2, ListNode(2, ListNode(3, None)))),
    ListNode(1, ListNode(100000, None))
]

expected_results = [
    6,
    7,
    100001
]

class Solution:
    def pairSum(self, head) -> int:
        array = []
        while True:
            # print(head)
            # print(head.next)
            array.append(head.val)
            if head.next != None:
                head = head.next
            else:
                break
        print(array)
        max = 0
        for i in range(0, int(len(array)/2)):
            if array[i] + array[-(i+1)] > max:
                max = array[i] + array[-(i+1)]
        return max


# Testing
for i in range(0, len(test_cases)):
    result = Solution.pairSum(Solution, test_cases[i])
    if result == expected_results[i]:
        print(f"==Test case {i+1} was valid")
        print(f"✔️  Got '{result}', expected {expected_results[i]}")
    else:
        print(f"==Test case {i+1} was INVALID")
        print(f"❌ Got '{result}', expected {expected_results[i]}")

