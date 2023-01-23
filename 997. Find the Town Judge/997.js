let testcases = [
    {
        n: 2,
        trust: [[1, 2]]
    },
    {
        n: 3,
        trust: [[1, 3], [2, 3]]
    },
    {
        n: 3,
        trust: [[1, 3], [2, 3], [3, 1]]
    }
]


/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function (n, trust) {
    let trusting = {}, trustees = {};
    for (let i = 1; i <= n; i++) {
        trusting[i] = 0;
        trustees[i] = 0;
    }
    for (let i = 0; i < trust.length; i++) {
        trusting[trust[i][0]] += 1;
        trustees[trust[i][1]] += 1;
    }
    for (let i = 1; i <= n; i++) {
        if (trustees[i] == n - 1 && trusting[i] == 0) {
            return i;
        }
    }
    return -1;
};



//Testing
for (let i = 0; i < testcases.length; i++) {
    caseNumber = i + 1;
    console.log(`Testing case ${caseNumber}`);
    console.log(testcases[i]);
    result = findJudge(testcases[i]["n"], testcases[i]["trust"]);
    switch (caseNumber) {
        case 1:
            if (result == 2) { console.log(`Test ${caseNumber} Passed`) }
            else { console.log(`Test ${caseNumber} Failed`) }
            break
        case 2:
            if (result == 3) { console.log(`Test ${caseNumber} Passed`) }
            else { console.log(`Test ${caseNumber} Failed`) }
            break
        case 3:
            if (result == -1) { console.log(`Test ${caseNumber} Passed`) }
            else { console.log(`Test ${caseNumber} Failed`) }
            break
    }
}