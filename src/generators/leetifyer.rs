pub struct Leetifyer {}

impl Leetifyer {
    pub fn new() -> Self {
        Leetifyer {

        }
    }
    
    pub fn leetify(&self, input: String) -> String {
        let mut out: Vec<char> = vec![];

        for c in input.chars() {
            if c == 'e' {
                out.push('3');
            }

            else {
                out.push(c);
            }
        }
        out.iter().collect()
    }
}