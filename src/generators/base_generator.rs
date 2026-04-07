use std::{fs::{self, File}, io::{BufRead, BufReader}};


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
}