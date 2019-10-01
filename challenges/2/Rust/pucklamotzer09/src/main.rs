use std::io;

fn main() {
    println!("Type in 5 integers to calculate their mean!");
    
    let mut integer = [1,2,3,4,5];

    for i in 1..=5 {
        println!("{}: ",i);
        let mut input = String::new();
        io::stdin().read_line(&mut input)
            .expect("Failed to read line");
        let input : i32 = input.trim().parse()
            .expect("Please type a number!");
        integer[i-1] = input;
    }

    let mut mean = 0;
    for i in integer.iter() {
        mean += i;
    }

    mean = mean / 5;

    println!("The mean is {}",mean);
}
