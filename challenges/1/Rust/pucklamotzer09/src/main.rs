extern crate rand;

use rand::Rng;

fn main() {
    let mut integer = [1,2,3,4,5,6,7,8,9,10];

    let mut i = 0;
    while i < 10  {
        integer[i] = rand::thread_rng().gen_range(1,1000);
        i+=1;
    }

    let mut sum = 0;
    for i in integer.iter() {
        sum += i;
    }
    println!("Sum: {}",sum);
}
