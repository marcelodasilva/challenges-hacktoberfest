use std::io;

fn main() {
    println!("Convert Fahrenheit to Celsius!");
    println!("Fahrenheit: ");
    
    let mut f = String::new();
    io::stdin().read_line(&mut f)
        .expect("Failed to read line");
    let f : f64 = f.trim().parse()
        .expect("Please type a number");
    let c = 5.0 * (f-32.0) / 9.0;

    println!("Celsius: {}°",c);
}
