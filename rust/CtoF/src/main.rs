use std::io;

fn main() {
    println!("type exit to exit");

    loop {
    
    let mut c = String::new();
    
        println!("input C:");

        io::stdin()
            .read_line(&mut c)
            .expect("Failed to read line");

        let c: u32 = match c.trim().parse() {
            Ok(num) => num,
            Err(_) => todo!(),
        };

        println!("f:{}",c * 9/5 + 32);
    };
}
