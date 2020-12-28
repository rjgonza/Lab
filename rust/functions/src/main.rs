fn main() {
    another_function(5, 6);
    let returned_data = some_function(1.2, 1);
    println!("returned_data: {}", returned_data);
}

fn another_function(x: i32, y: i32) {
    println!("The value of x is: {}", x);
    println!("The value of y is: {}", y);
}

fn some_function(_param_a: f32, _param_b: i128) -> f32 {
    println!("I'm in some_function!");
    1 as f32 // 1. or 1_f32 or 1f32
}
