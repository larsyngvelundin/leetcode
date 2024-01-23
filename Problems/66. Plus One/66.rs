fn plus_one(digits: &mut Vec<i32>) -> Vec<i32> {
    for i in (0..digits.len()).rev() {
        if digits[i] == 9 {
            digits[i] = 0;
        } else {
            digits[i] += 1;
            return digits.to_vec();
        }
    }
    digits.insert(0, 1);
    digits.to_vec()
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
        let result = plus_one(&mut test_cases[i]);
        if result == expected_results[i] {
            println!("==Test case {} was valid", i+1);
            println!("Got '{:?}', expected {:?}", result, expected_results[i]);
        } else {
            println!("==Test case {} was INVALID", i+1);
            println!("Got '{:?}', expected {:?}", result, expected_results[i]);
        }
    }
}

