
use std::collections::HashMap;

fn seek_bag(rules:&HashMap<String, Vec<String>>, bag:&String) -> bool {
    let mut found = false;

    if !rules.contains_key(bag) || rules[bag][0] == "no other"{
        found = false;
    } else {
        for b in &rules[bag] {
            if b.contains("shiny gold"){
                found = true;
            } else {
                let mut it = b.split(" ");
                let _num:usize = it.next().unwrap().parse().unwrap();
                let mut color = it.next().unwrap().to_string();
                color.push_str(it.next().unwrap());
                found = seek_bag(rules, &color );
            }
            if found { 
                break; 
            }
        }
    }
    found
    
}

fn seek_bag_2(rules:&HashMap<String, Vec<String>>, bag:&String, current_total: usize) -> usize {
    let mut nb_bags = 0;

    if !rules.contains_key(bag) || rules[bag][0] == "no other"{
        nb_bags = 0;
    } else {
        for b in &rules[bag] {
            let mut it = b.split(" ");
            let num:usize = it.next().unwrap().parse().unwrap();
            let mut color = it.next().unwrap().to_string();
            color.push_str(it.next().unwrap());

            nb_bags += current_total * seek_bag_2(rules, &color, num)

        }
    }

    nb_bags + current_total 
}

fn bag_capacity(pipi:HashMap<String, Vec<String>>) -> usize{
    let total = seek_bag_2(&pipi, &String::from("shinygold"), 1);
    total - 1 
}

fn find_gold_bag(rules:&HashMap<String, Vec<String>>) -> i32{
    let mut counter = 0;
    for (k, _) in rules.iter() {

        if seek_bag(rules, &k) {
            counter += 1;
        }

    }
    counter
}

fn main() {
    let input = std::fs::read_to_string("input.txt").unwrap();
    let rules = input.split("\n");
    let mut rules_map:HashMap<String, Vec<String>> = HashMap::new();

    for rule in rules{
        let mut r = rule.split(".").next().unwrap().split(" bags contain ");
        let mut key = r.next().unwrap().to_string();
        let values: Vec<String> = r.next()
                                   .unwrap()
                                   .split(", ")
                                   .map(|s| s.to_string().split(" bag")
                                                         .next()
                                                         .unwrap()
                                                         .to_string())
                                                         .collect();

        key.retain(|c| !c.is_whitespace());


        rules_map.insert(key,values);
    
    }

   println!("Part 1: {}", find_gold_bag(&rules_map));
   println!("Part 2: {}", bag_capacity(rules_map));

}

