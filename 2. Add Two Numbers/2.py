class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


test_cases = [
    [
        ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3))),
        ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
    ],
    # [[2, 4, 3], [5, 6, 4]],
    [
        ListNode(),
        ListNode()
    ],
    # [[0], [0]],
    [
        ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(
            val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9))))))),
        ListNode(val=9, next=ListNode(
            val=9, next=ListNode(val=9, next=ListNode(val=9))))
    ]
    # [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]]
]


expected_results = [
    ListNode(val=7, next=ListNode(val=0, next=ListNode(val=8))),
    # [7, 0, 8],
    ListNode(),
    # [0],
    ListNode(val=8, next=ListNode(
        val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(next=ListNode(next=ListNode(next=ListNode(val=1))))))))
    # [8, 9, 9, 9, 0, 0, 0, 1]
]


class Solution:
    def addTwoNumbers(self, l1, l2):
        int1 = 0
        mult = 1
        while (l1 != None):
            int1 += l1.val * mult
            l1 = l1.next
            mult *= 10
        int2 = 0
        mult = 1
        while (l2 != None):
            int2 += l2.val * mult
            l2 = l2.next
            mult *= 10
        int_sum = int1 + int2
        digits = [int(digit) for digit in str(int_sum)]
        sum_nodes = ListNode(val=digits[0])
        for i in range(1, len(digits)):
            sum_nodes = ListNode(val=digits[i], next=sum_nodes)
        return sum_nodes


def list_same(l1, l2):
    while (l1 != None):
        if (l1.val == l2.val):
            l1 = l1.next
            l2 = l2.next
        else:
            return False
    return True


    # Testing
for i in range(0, len(test_cases)):
    print("==================================")
    result = Solution.addTwoNumbers(
        Solution, test_cases[i][0], test_cases[i][1])
    if list_same(result, expected_results[i]):
        print(f"==Test case {i+1} was valid")
        print(f"✔️  Got '{result}', expected {expected_results[i]}")
    else:
        print(f"==Test case {i+1} was INVALID")
        print(f"❌ Got '{result}', expected {expected_results[i]}")
