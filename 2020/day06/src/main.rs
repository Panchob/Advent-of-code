use std::collections::HashSet;
use std::collections::HashMap;


fn parse_answers(input: &str) -> i32 {
    let mut letters:HashSet<char> = HashSet::new();
    for c in input.chars() {
        if c.is_alphabetic() {
            letters.insert(c);
        }
       
    }

    letters.len() as i32
}

fn parse_answer_count_1(input: &str) -> i32 {
    let mut letters: HashMap<char, i32> = HashMap::new();
    let mut counter = 0;
    let mut ans = 0;

    for line in input.split("\r\n") {
        counter += 1;
        for c in line.chars() {
            if c.is_alphabetic() {
                *letters.entry(c).or_insert(0) += 1;
            }
        }
    }

    for v in letters.values() {
        if *v == counter {
            ans += 1;
        }

    }
    ans
}

fn main() {
    let input = std::fs::read_to_string("input.txt").unwrap();
    let ans:i32 = input.trim().split("\r\n\r\n").map(parse_answers).sum();
    println!("Part 1: {}", ans);
    let ans:i32 = input.trim()
                       .split("\r\n\r\n")
                       .map(parse_answer_count_1)
                       .sum();
    println!("Part 2: {}", ans);
}