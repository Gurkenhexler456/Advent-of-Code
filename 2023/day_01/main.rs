use std::fs::File;
use std::io::{BufReader, BufRead};

const NUMBER_WORDS: [&str; 9] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

fn main() {

    let file = File::open("input.txt").expect("Cannot open file");
    let reader = BufReader::new(file);
    let lines = reader.lines();
    let mut sum: u32 = 0;

    for line in lines {

        sum += match line {
            Ok(l) => get_number(&l), 
            _ => 0,
        }
    }

    println!("Sum: {sum}");
}


fn get_first_number(line: &String) -> u32 {

    let mut first_digit: (usize, u32) = (line.len(), 0);

    for (i, el) in line.bytes().enumerate() {
        if el.is_ascii_digit() {
            let n: u32 = (el - b'0').into();
            first_digit = (i, n);
            break;
        }
    }

    
    let slice = line;
    for (i, word) in NUMBER_WORDS.iter().enumerate() {
        match slice.find(word) {
            Some(x) => {
                if x < first_digit.0 {
                    let value: u32 = (i + 1) as u32;
                    first_digit = (x, value);
                }
            }
            None => (),
        }
    }

    first_digit.1
}

fn get_last_number(line: &String) -> u32 {

    let mut last_digit: (usize, u32) = (0, 0);

    for (i, el) in line.bytes().rev().enumerate() {
        if el.is_ascii_digit() {
            let n: u32 = (el - b'0').into();
            last_digit = (line.len() - i - 1, n);
            break;
        }
    }

    
    let slice = line;
    for (i, word) in NUMBER_WORDS.iter().enumerate() {
        match slice.rfind(word) {
            Some(x) => {
                if x >= last_digit.0 {
                    let value: u32 = (i + 1) as u32;
                    last_digit = (x, value);
                }
            }
            None => (),
        }
    }

    last_digit.1
}



fn get_number(line: &String) -> u32 {
    let first = get_first_number(&line);
    let last = get_last_number(&line);
    first * 10 + last
}