testCases = [{ 'nums': [-1, 0, 3, 5, 9, 12], 'target': 9 },
{ 'nums': [-1, 0, 3, 5, 9, 12], 'target': 2 },
{ 'nums': [5], 'target': 5 },
{ 'nums': [5, 6], 'target': 5 },
{ 'nums': [2, 5], 'target': 5 },
{ 'nums': [-1, 0, 5], 'target': 5 }
];
expectedResults = [4, -1, 0, 0, 1, 2];


var search = function (nums, target) {
    let start = 0;
    let end = nums.length - 1;
    let pivot = parseInt(end / 2);
    do {
        if (nums[pivot] == target) { return pivot } else {
            if (nums[pivot] > target) {
                end = pivot - 1;
                pivot = parseInt((end - start) / 2) + start;
            }
            else if (start != pivot) {
                start = pivot + 1;
                pivot = parseInt((end - start) / 2) + start;
            }
            else {
                pivot = end;
            }
        }
    } while (start <= end);
    return -1;
};

var searchFromPseudo = function (nums, target) {
    let start = 0
    let end = nums.length - 1
    while (start <= end) {
        let pivot = Math.floor((start + end) / 2);
        if (nums[pivot] < target) {
            start = pivot + 1;
        }
        else if (nums[pivot] > target) {
            end = pivot - 1;
        }
        else {
            return pivot;
        }
    }
    return -1;
}

// # Testing
for (let i = 0; i < testCases.length; i++) {
    let result = search(testCases[i]['nums'], testCases[i]['target']);
    if (result == expectedResults[i]) {
        console.log(`==Test case ${i + 1} was valid`)
        console.log(`✅ Got "${result}", expected "${expectedResults[i]}"`)
    }
    else {
        console.log(`==Test case ${i + 1} was INVALID`)
        console.log(`❌ Got "${result}", expected "${expectedResults[i]}"`)
    }
}