#![allow(dead_code)]

use std::time::{Instant};

struct Data {
    a: u64,
    b: u64,
}

fn main() {
    let start_time = Instant::now();
    //
    {
        let mut vec = Vec::with_capacity(100_000);
        for i in 0..100_000 {
            vec.push(Box::new(Data { a: i as u64, b: i as u64 / 2 }));
        }
    }
    //
    let end_time = Instant::now();
    let elapsed_time = end_time.duration_since(start_time).as_micros();
    println!("{}", elapsed_time);
}