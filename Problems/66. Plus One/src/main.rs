fn plus_one(digits: Vec<i32>) -> Vec<i32> {
    let mut result: Vec<i32> = digits.to_vec();
    for i in (0..result.len()).rev() {
        if result[i] == 9 {
            result[i] = 0;
        } else {
            result[i] += 1;
            return result;
        }
    }
    let mut new_result = vec![1];
    new_result.extend(result.iter());
    new_result
}

fn main() {
    let test_cases = vec![
        vec![1, 2, 3],
        vec![4, 3, 2, 1],
        vec![9],
        vec![5, 9, 9],
        vec![9, 9],
        vec![9, 8, 9]
    ];
    let expected_results = vec![
        vec![1, 2, 4],
        vec![4, 3, 2, 2],
        vec![1, 0],
        vec![6, 0, 0],
        vec![1, 0, 0],
        vec![9, 9, 0]
    ];

    for i in 0..test_cases.len() {
        println!("==================================");
        let test_case: Vec<i32> = test_cases[i].to_vec();
        let result = plus_one(test_case);
        if result == expected_results[i] {
            println!("==Test case {} was valid", i+1);
            println!("Got '{:?}', expected {:?}", result, expected_results[i]);
        } else {
            println!("==Test case {} was INVALID", i+1);
            println!("Got '{:?}', expected {:?}", result, expected_results[i]);
        }
    }
}

