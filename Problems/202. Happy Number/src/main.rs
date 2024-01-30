pub fn is_happy(n: i32) -> bool {
    let mut n: u32 = n as u32;
    let mut past_numbers: Vec<u32> = vec![n];
    loop {
        if n == 1 { return true; }
        let n_list: Vec<u32> = n.to_string()
            .chars()
            .map(|c| c.to_digit(10).unwrap())
            .collect();
        let mut new_n: u32 = 0; 
        for i in 0..n_list.len() {
            new_n += n_list[i] * n_list[i];
        }
        n = new_n;
        if past_numbers.contains(&n){
            return false;
        }
        past_numbers.push(n)
    }
}

fn main() {

    let test_cases:Vec<i32> = vec![
        19,
        2
    ];

    let expected_results:Vec<bool> = vec![
        true,
        false
    ];

    for i in 0..test_cases.len() {
        println!("==================================");
        let test_case: i32 = test_cases[i];
        let result = is_happy(test_case);
        if result == expected_results[i] {
            println!("==Test case {} was valid", i+1);
            println!("Got '{:?}', expected {:?}", result, expected_results[i]);
        } else {
            println!("==Test case {} was INVALID", i+1);
            println!("Got '{:?}', expected {:?}", result, expected_results[i]);
        }
    }
}
