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

fn part_1(vector: &Vec<i32>) -> i32 {
    let mut res = 0;
    for x in vector.iter() {
        for y in vector.iter() { 
            if x + y == 2020 {
                res = x * y
            }
        }   
    }
    res   
}

fn part_2(vector: &Vec<i32>) -> i32 {
    let mut res = 0;
    for x in vector.iter() {
        for y in vector.iter() { 
            for z in vector.iter() {
                if x + y + z == 2020 {
                    res = x * y * z
                }
            }
        }   
    }
    res   
}

fn main() {
    let lines = lines_from_file("input.txt");
    let mut vector = vec![];
    for line in lines {
        vector.push(line.parse::<i32>().unwrap());
    }
    println!("Part 1: {}", part_1(&vector));
    println!("Part 2: {}", part_2(&vector));
}