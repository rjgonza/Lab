fn main() {
    another_function(5, 6);
    let returned_data = some_function(1.2, 1);
    println!("returned_data: {}", returned_data);

    some_procedure(2.3, 1);

    some_str_procedure("test");

    let string_slice_var: &str = "Howdy!";
    some_str_procedure(string_slice_var);

    let string_var = String::from("I'm a REAL String ;)");
    some_str_procedure(&string_var);

    some_string_procedures(string_var);

    let f = last_char(String::from("Hello"));
    println!("{}", f)
}

fn some_string_procedures(param: String) {
    println!("I'm in some_string_procedure wih param {}", param);
}

fn another_function(x: i32, y: i32) {
    println!("The value of x is: {}", x);
    println!("The value of y is: {}", y);
}

fn some_str_procedure(param: &str) {
    println!("I'm in some_str_procedure with param {}", param);
}

fn some_procedure(param_a: f32, param_b: i128) {
    println!("I'm in some_procedure with a {} b {}", param_a, param_b);
}

fn some_function(param_a: f32, param_b: i128) -> f32 {
    println!("I'm in some_function!");

    if param_a < 100. {
        let returned_var = 10.1 * param_a + param_b as f32;

        returned_var
    } else {
        -1.
    }
    // 1 as f32 // 1. or 1_f32 or 1f32
}

fn last_char(string: String) -> char {
    if string.is_empty() {
        return 'p';
    }
    string.chars().next_back().unwrap()
}
