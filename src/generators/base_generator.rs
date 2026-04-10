use std::{fs::{File}, io::{BufRead, BufReader}};

use rand::{RngExt, rngs::ThreadRng};

use crate::generators::leetifyer::Leetifyer;


pub struct BaseGenerator {
    pub words: Vec<String>,
    rng: ThreadRng,
    leet: Leetifyer
}

impl BaseGenerator {
    pub fn new(word_list: &str) -> Self {
        let file = File::open(word_list).expect("no such wordlist file");
        let buf = BufReader::new(file);
        let words: Vec<String> = buf.lines().map(|l| l.expect("Could not parse line")).collect();
        BaseGenerator {
            words,
            rng: rand::rng(),
            leet: Leetifyer::new(0.7_f32)
        }
    }

    pub fn generate_word(&mut self) -> String {
        let out = format!("{}{}", self.leet.leetify(self.words[self.rng.random_range(0..self.words.len())].to_string()), self.rng.random_range(0..9));
        out
    }
}