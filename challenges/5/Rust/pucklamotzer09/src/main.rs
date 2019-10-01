use std::io;

fn main() {
    println!("Type in two numbers to print the largest one");
    let mut input = String::new();
    io::stdin().read_line(&mut input)
        .expect("Failed to read line");
    let i1 : i32 = input.trim().parse()
        .expect("Please type in a number");
    let mut input = String::new();
    io::stdin().read_line(&mut input)
        .expect("Failed to read line");
    let i2 : i32 = input.trim().parse()
        .expect("Please type in a number");
    if i1 > i2 {
        println!("{} is bigger than {}",i1,i2);
    } else if i2 > i1 {
        println!("{} is bigger than {}",i2,i1);
    } else {
        println!("{} is equal to {}",i1,i2);
    }
}
