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

fn is_lower(c: char) -> bool {
    c == 'F' || c == 'L'
}

fn find_seat(line: &str, upper: &i32) -> i32 {
    let u = *upper;
    let mut bracket = (0, u);
    for c in line.chars() {
        if is_lower(c) {
            bracket.1 = bracket.1 - 1 - (bracket.1 - bracket.0) / 2;
        } else {
            bracket.0 = bracket.1 - (bracket.1 - bracket.0) / 2;
        }
    }

    bracket.1
}

fn seat_id(row: i32, col: i32) -> i32 {
    row * 8 + col
}

fn main() {
    let lines = lines_from_file("input.txt");
    let mut ans: Vec<i32> = vec![];

    for line in &lines {
        let row = find_seat(&line[..7], &127);
        let col = find_seat(&line[7..], &7);
        ans.push(seat_id(row, col));
    }

    println!("Part 1: {}", ans.iter().max().unwrap());
    
    let res = ans.iter().max().and_then(|max_id| {
        (1..=*max_id).find(|id_ref| {
            let id = *id_ref;
            !ans.contains(&id) && ans.contains(&(id-1)) && ans.contains(&(id+1))
        })
    }).unwrap();

    println!("Part 2: {}", res);
}

