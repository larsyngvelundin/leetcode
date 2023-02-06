let testCases = [
    {
        n: 3,
        nums: [2,5,1,3,4,7]
    },
    {
        n: 4,
        nums: [1,2,3,4,4,3,2,1]
    },
    {
        n: 2,
        nums: [1,1,2,2]
    }
];
let expectedResults = [
    [2,3,5,4,1,7],
    [1,4,2,3,3,2,4,1],
    [1,2,1,2]
];


/**
 * @param {number} n
 * @param {number[][]} nums
 * @return {number}
 */
var shuffle = function (nums, n) {
    let newArray = [];
    for(let i = 0; i < n; i++){
        newArray.push(nums[i]);
        newArray.push(nums[i+n]);
    }
    return newArray;
};


for (let i = 0; i < testCases.length; i++) {
    let result = shuffle(testCases[i]['nums'],testCases[i]['n']);
    if (result == expectedResults[i]) {
        console.log(`==Test case ${i + 1} was valid`)
        console.log(`✔️ ${result}, expected ${expectedResults[i]}`)
    }
    else {
        console.log(`==Test case ${i + 1} was INVALID`)
        console.log(`❌ ${result}, expected ${expectedResults[i]}`)
    }
}