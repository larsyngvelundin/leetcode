pub fn add_binary(a: String, b: String) -> String {
    let achars: Vec<char> = a.chars().rev().collect();
    let bchars: Vec<char> = b.chars().rev().collect();
    let len = std::cmp::max(achars.len(), bchars.len());
    if bchars.len() > achars.len(){
        let (achars, bchars) = (bchars.clone(), achars.clone());
    }
    let mut carry_over: u32 = 0;
    let mut newchars: Vec<char> = vec![];
    for i in 0..len {
        let mut current: u32 = 0;
        if i < bchars.len(){
            if bchars[i] == '1' { current += 1;}
        }
        if i < achars.len(){
            if achars[i] == '1' { current += 1;}
        }
        current += carry_over;
        if current & 1 == 1{
            newchars.push('1');
            if current == 3{ carry_over = 1; } else{carry_over = 0;}
        }
        else{
            newchars.push('0');
            if current == 2 {carry_over = 1;} else {carry_over = 0;}
        }
    }
    if carry_over == 1{
        newchars.push('1');
    }
    newchars.iter().rev().collect::<String>()
}

fn main() {
    let test_cases = vec![
        vec!["11", "1"],
        vec!["1010", "1011"],
        vec!["11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","1"],
        vec!["10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101", "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"]
    ];
    let expected_results = vec![
        "100",
        "10101",
        "100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000"
    ];
    for i in 0..test_cases.len() {
        println!("==================================");
        let a = test_cases[i][0].to_owned();
        let b = test_cases[i][1].to_owned();
        let result = add_binary(a, b);
        if result == expected_results[i] {
            println!("==Test case {} was valid", i+1);
            println!("Got {:?}, expected {:?}", result, expected_results[i]);
        } else {
            println!("==Test case {} was INVALID", i+1);
            println!("Got {:?}, expected {:?}", result, expected_results[i]);
        }
    }
}