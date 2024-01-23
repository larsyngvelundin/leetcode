let testCases = [
    {
        target: 9,
        nums: [2, 7, 11, 15]
    },
    {
        target: 6,
        nums: [3, 2, 4]
    },
    {
        target: 6,
        nums: [3, 3]
    }
];
let expectedResults = [[0, 1], [1, 2], [0, 1]];


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                return [i, j];
            }
        }
    }
};



//Testing
for (let i = 0; i < testCases.length; i++) {
    let caseNumber = i + 1;
    console.log(`Testing case ${caseNumber}`);
    console.log(testCases[i]);
    let result = twoSum(testCases[i]["nums"], testCases[i]["target"]);
    console.log("result", result);
    console.log("expected result", expectedResults[i]);

    let outcomeSuccess = true;
    for (let j = 0; j < 2; j++) {
        if (result[j] != expectedResults[i][j]) {
            outcomeSuccess = false;
        }
    }
    if (outcomeSuccess) {
        console.log(`Test case ${caseNumber} is valid`)
    }
    else {
        console.log(`Test case ${caseNumber} is FAILED`)
    }
    console.log("=================");
}