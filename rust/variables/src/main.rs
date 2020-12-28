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

    println!("{} {} {} {} {} {}", x, y, t, f, c, z);

    println!("{}", heart_eyes_cat);

    let tup = (500, 6.4, 1);

    let (x, y, z) = tup;

    println!("{} {} {}", x, y, z);
    println!("The value of y is: {}", y);

    let x: (i32, f64, u8) = (500, 6.4, 1);

    let five_hundred = x.0;

    let six_point_four = x.1;

    let one = x.2;

    println!("{} {} {}", five_hundred, six_point_four, one);

    let example_str: &str = "Howdy";
    let example_string: String = String::from("Partner");

    let string_from_str: String = example_str.to_string();
    let string_from_str2: String = "Some hardcoded string".to_string();

    let string_from_hardcoded = String::from("Some hardcoded");
    let string_from_str_var = String::from(example_str);

    let str_from_string: &str = &example_str;

    let combine_string_literals = ["first", "second"].concat();
    let combine_with_format_macro = format!("{} {}", "first", "second");

    let string_plus_str = example_string + example_str;

    println!("{} {}", string_from_str, string_from_str2);
    println!("{} {}", string_from_hardcoded, string_from_str_var);
    println!("{}", str_from_string);
    println!("{} {}", combine_string_literals, combine_with_format_macro);
    println!("{}", string_plus_str);

    let mut mut_string = String::new();
    mut_string.push_str(example_str);
    mut_string.push_str("Some hardcoded literal");
    mut_string.push('m');

    println!("{}", mut_string);

    let a = String::from("a");
    let b = String::from("b");
    let combined = a + &b + &mut_string;

    println!("{}", combined);

    let str_from_substring: &str = &example_str[0..2];

    println!("{}", str_from_substring);

    let str_from_substring: &str = &example_str[0..=4];

    println!("{}", str_from_substring);

    let char_by_index = &example_str.chars().nth(1);

    println!("{:?}", char_by_index);

    match char_by_index {
        Some(c) => println!("Found a char {}", c),
        None => {}
    }

    if let Some(c) = example_str.chars().nth(2) {
        println!("Found a char {}", c);
    }
}
