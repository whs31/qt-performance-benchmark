#![allow(dead_code)]

use std::time::Instant;

struct Data {
    a: u64,
    b: u64,
}

impl Data {
    fn new(x: usize) -> Data {
        Data {
            a: x as u64 / 2,
            b: x as u64 / (x % 2 + 1) as u64,
        }
    }
}

fn main() {
    let start_time = Instant::now();
    //
    let mut vec: Vec<Data> = Vec::new();
    for i in 0..5_000_000 {
        vec.push(Data::new(i));
    }
    //
    let end_time = Instant::now();
    let elapsed_time = end_time.duration_since(start_time).as_millis();
    println!("{}", elapsed_time);
}
