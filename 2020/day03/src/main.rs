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

fn count_trees(slope:(usize, usize)) -> usize {
    let lines = lines_from_file("input.txt");
    let mut pos = 0;
    let width = lines[0].chars().count();
    let mut count = 0;
    let mut next_line = 0;
    let mut current_line = 0;

    for line in &lines {
        if current_line == next_line {
            if line.chars().nth(pos).unwrap() == '#' {
                count += 1;
            }
            next_line += slope.1;
            pos = (pos + slope.0) % width;
        }
        current_line += 1;
    }
    count
}

fn main() {
    let part1 = count_trees((3, 1));
    println!("Part 1: {}", part1);

    let part2_data = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];
    let mut part2:Vec<usize> = vec![];
    for data in part2_data.iter() {
        part2.push(count_trees(*data))
    }
    let mult:usize = part2.into_iter().product();
    println!("Part 2: {}", mult);
}
