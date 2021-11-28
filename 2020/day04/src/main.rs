struct Passport {
    byr: Option<String>,
    iyr: Option<String>,
    eyr: Option<String>,
    hgt: Option<String>,
    hcl: Option<String>,
    ecl: Option<String>,
    pid: Option<String>,
    cid: Option<String>
}

impl Passport {
    fn constructor() -> Self {
        Passport {
            byr: None, iyr: None, eyr: None, hgt: None,
            hcl: None, ecl: None, pid: None, cid: None
        }
    }
}

fn parse_passport(input: &str) -> Passport {
    let mut passport = Passport::constructor();

    for text in input.replace("\n", " ").split(" ") {
        let field: Vec<&str> = text.split(":").collect();
        let value = field[1].to_string(); 
        match field[0] {
            "byr" => { passport.byr = Some(value) },
            "iyr" => { passport.iyr = Some(value) },
            "eyr" => { passport.eyr = Some(value) },
            "hgt" => { passport.hgt = Some(value) },
            "hcl" => { passport.hcl = Some(value) },
            "ecl" => { passport.ecl = Some(value) },
            "pid" => { passport.pid = Some(value) },
            "cid" => { passport.cid = Some(value) },
            _ => {},
        }
    }
    passport
}

fn validate_passport(passport: &Passport) -> bool {
    passport.byr.is_some() &&
    passport.iyr.is_some() &&
    passport.eyr.is_some() &&
    passport.hgt.is_some() &&
    passport.hcl.is_some() &&
    passport.ecl.is_some() &&
    passport.pid.is_some()
}

fn main() {
    let input = std::fs::read_to_string("input.txt").unwrap();
    let passports: Vec<Passport> = input.trim().split("\r\n\r\n").map(parse_passport).collect();


    let mut counter = 0;
    for passport in passports {
        if validate_passport(&passport) {
            counter += 1;
        }
    }

    println!("{}", counter)
}


