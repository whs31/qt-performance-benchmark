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
    let mut vec: Vec<Data> = Vec::new();
    for i in 0..1_000_000 {
        vec.push(Data::new(i));
    }
}