use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

fn lines_from_file(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

fn main() {
    let lines = lines_from_file("input.txt");
    let mut count = 0;
    for line in &lines {
        let mut v = line.split(" ");
        let mut limits = v.next().unwrap().split("-");
        let min = limits.next().unwrap().parse().unwrap();
        let max = limits.next().unwrap().parse().unwrap();
        let letter = v.next().unwrap().chars().next().unwrap();
        let password = String::from(v.next().unwrap());
        let letter_match = password.matches(letter).count() as u32;
        if letter_match >= min && letter_match <= max {
            count += 1;
        } 
    }
    println!("part1: {}", count);
    count = 0;
    for line in &lines {
        let mut v = line.split(" ");
        let mut indexes = v.next().unwrap().split("-");
        let first_index: usize = indexes.next().unwrap().parse().unwrap();
        let second_index: usize = indexes.next().unwrap().parse().unwrap();
        let letter = v.next().unwrap().chars().next().unwrap();
        let password = String::from(v.next().unwrap());
        let iter_password = password.as_bytes();
        if iter_password[first_index - 1] != iter_password[second_index - 1] && 
           (iter_password[first_index - 1] as char == letter || iter_password[second_index - 1] as char == letter){
            count += 1;
        } 
    }
    println!("part2: {}", count);
}
