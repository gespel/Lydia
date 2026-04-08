use std::{fs::{File}, io::{BufRead, BufReader}};

use rand::RngExt;


pub struct BaseGenerator {
    pub words: Vec<String>
}

impl BaseGenerator {
    pub fn new(word_list: &str) -> Self {
        let file = File::open(word_list).expect("no such wordlist file");
        let buf = BufReader::new(file);
        let words: Vec<String> = buf.lines().map(|l| l.expect("Could not parse line")).collect();
        BaseGenerator {
            words
        }
    }

    pub fn generate_word(&self) -> String {
        let mut rng = rand::rng();
        let out = format!("{}{}", self.words[rng.random_range(0..self.words.len())], rng.random_range(0..9));
        out
    }
}