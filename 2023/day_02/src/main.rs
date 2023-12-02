use std::fs::File;
use std::io::{BufReader, BufRead};

use std::collections::HashMap;

fn main() {
    
    let file = File::open("input/input.txt").expect("Cannot open File");
    let reader = BufReader::new(file);
    let lines = reader.lines();

    let mut config: HashMap<String, u32> = HashMap::new();
    config.insert(String::from("red"), 12);
    config.insert(String::from("green"), 13);
    config.insert(String::from("blue"), 14);


    let mut sum_id = 0;
    let mut sum_power = 0;

    for line in lines {
        let (id, power) = match line {
            Ok(x) => process_line(&x, &config),
            _ => (0, 0),
        };

        sum_id += id;
        sum_power += power;
    }

    println!("ID sum: {sum_id}");
    println!("Power sum: {sum_power}");
}

fn process_line(line: &str, config: &HashMap<String, u32>) -> (u32, u32) {

    let game_line: Vec<&str> = line.split(':').collect();
    let game_head: Vec<&str> = game_line[0].split(' ').collect();
    let id: u32 = game_head[1].trim().parse().expect("No Game Head");
    let game_steps: Vec<&str> = game_line[1].split(';').collect();

    let mut map = HashMap::new();

    map.insert(String::from("red"), 0);
    map.insert(String::from("green"), 0);
    map.insert(String::from("blue"), 0);

    let mut possible = true;

    for step in game_steps {
        let cubes: Vec<&str> = step.split(',').collect();


        for cube in cubes {
            let info: Vec<&str> = cube.trim().split(' ').collect();

            let amount: u32 = info[0].trim().parse().expect("parsing failed");
            let color = info[1].trim();

            match map.get(color).copied() {
                Some(x) => {
                    if let Some(max) = config.get(color).copied() {
                        if max < amount {
                            possible = false;
                        }
                    }

                    if amount > x {
                        map.insert(color.to_string(), amount);
                    }
                }
                None => println!("unknown color: {color}"),
            };
        }


    }

    let mut power = 1;

    for (key, value) in &map {
        power *= value;
    }

    if possible { (id, power) } else { (0, power) } 
}