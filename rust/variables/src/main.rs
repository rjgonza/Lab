fn main() {
    let mut x = 5;
    println!("The value of x is: {}", x);
    x = 6;
    println!("The value of x is: {}", x);

    let x = 5;

    let x = x + 1;

    let x = x * 2;

    println!("The value of x is: {}", x);

    let x = 2.0;

    let y: f32 = 3.0;

    let t = true;

    let f: bool = false;

    let c = 'z';
    let z = 'Z';
    let heart_eyes_cat = '😻';

    println!("{}", heart_eyes_cat);

    let tup = (500, 6.4, 1);

    let (x, y, z) = tup;

    println!("The value of y is: {}", y);

    let x: (i32, f64, u8) = (500, 6.4, 1);

    let five_hundred = x.0;

    let six_point_four = x.1;

    let one = x.2;
}