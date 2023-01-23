let testCases = ["III", "LVIII", "MCMXCIV", "IX", "XC"];
let expectedResults = [3, 58, 1994, 9, 90];




/**
 * @param {string} s
 * @return {number}
 */
let symbolLookup = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
let modifiers = ["I", "X", "C"];
var romanToInt = function (s) {
    let result = 0;
    for (let i = 0; i < s.length; i++) {
        if (i > 0 && modifiers.includes(s[i - 1]) && symbolLookup[s[i]] > symbolLookup[s[i - 1]]) {
            result += symbolLookup[s[i]] - symbolLookup[s[i - 1]];
        }
        else if (modifiers.includes(s[i]) && i < s.length - 1) {
            if (symbolLookup[s[i]] == symbolLookup[s[i + 1]]) {
                result += symbolLookup[s[i]];
            }
        }
        else if (i > 0 && modifiers.includes(s[i - 1]) && symbolLookup[s[i]] > symbolLookup[s[i - 1]]) {
            result += symbolLookup[s[i]] - symbolLookup[s[i - 1]];
        }
        else {
            result += symbolLookup[s[i]];
        }
    }
    return result;
};


//Testing
for (let i = 0; i < testCases.length; i++) {
    console.log("===========================");
    caseNumber = i + 1;
    console.log(`Testing case ${caseNumber}`);
    result = romanToInt(testCases[i]);
    console.log(`Result: ${result}`);
    if (result == expectedResults[i]) {
        console.log(`Test ${caseNumber}: Valid`);
    }
    else {
        console.log(`Test ${caseNumber}: INVALID`);
        console.log(`Expected Result: ${expectedResults[i]}`);
    }

}