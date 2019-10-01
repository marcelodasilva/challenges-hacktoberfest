use std::io;

fn main() {
    println!("Calculate the fibonacci sequence to the Nth element!");
    println!("N: ");

    let mut n = String::new();
    io::stdin().read_line(&mut n)
        .expect("Failed to read line");
    let n : usize = n.trim().parse()
        .expect("Please type in a unsigned number");

    let mut fibonacci = [0,1];
    for i in 0..n {
        if i == 0 || i == 1 {
            print!("{} ",fibonacci[i]);
        } else {
            let current = fibonacci[0]+fibonacci[1];
            print!("{} ",current);
            fibonacci[0] = fibonacci[1];
            fibonacci[1] = current;
        }
    }
}
