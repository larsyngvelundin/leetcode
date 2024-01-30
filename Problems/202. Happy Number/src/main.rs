
pub fn is_happy(n: i32) -> bool {
    let mut past_numbers: Vec<i32> = vec![];
    past_numbers.push(n);


    println!("numbers: {}", past_numbers.len());
    true
}
pub fn number_to_digit_vec(n: i32) -> Vec<u32> {
    n.to_string()
        .chars()
        .map(|c| c.to_digit(10).unwrap())
        .collect()
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

    // println!("Hello, world!");
    // let resu : bool = is_happy(1);
    // if resu == true{
    //     println!("True")
    // }

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
