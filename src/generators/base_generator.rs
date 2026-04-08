use std::{fs::{File}, io::{BufRead, BufReader}};

use rand::{RngExt, rngs::ThreadRng};


pub struct BaseGenerator {
    pub words: Vec<String>,
    rng: ThreadRng
}

impl BaseGenerator {
    pub fn new(word_list: &str) -> Self {
        let file = File::open(word_list).expect("no such wordlist file");
        let buf = BufReader::new(file);
        let words: Vec<String> = buf.lines().map(|l| l.expect("Could not parse line")).collect();
        BaseGenerator {
            words,
            rng: rand::rng()
        }
    }

    pub fn generate_word(&mut self) -> String {
        let out = format!("{}{}", self.words[self.rng.random_range(0..self.words.len())], self.rng.random_range(0..9));
        out
    }
}