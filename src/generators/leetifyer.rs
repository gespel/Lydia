use rand::{RngExt, rngs::ThreadRng};


pub struct Leetifyer {
    rng: ThreadRng,
    probability: f32
}

impl Leetifyer {
    pub fn new(probability: f32) -> Self {
        Leetifyer {
            rng: rand::rng(),
            probability
        }
    }
    
    pub fn leetify(&mut self, input: String) -> String {
        let mut out: Vec<char> = vec![];

        for c in input.chars() {
            let r: f32 = self.rng.random_range(0_f32..1_f32);
            
            if r < self.probability {
                if c == 'e' {
                    out.push('3');
                }
                else if c == 'a' {
                    out.push('4');
                }

                else {
                    out.push(c);
                }
            }
            else {
                out.push(c);
            }
            
        }
        out.iter().collect()
    }
}