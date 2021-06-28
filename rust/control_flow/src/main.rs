fn main() {
    if 1 == 2 {
        println!("math is broken");
    } else {
        println!("everything is fine");
    }

    let formal: bool = true;
    let greeting: () = if formal {
        println!("Good evening!");
    } else {
        println!("Hey, friend!");
    };

    let number = 6;

    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else {
        println!("Number is not divisible by 3 or 4");
    }

    let boolean = true;

    let binary: i32 = match boolean {
        false => 0,
        true => 1,
    };
}
