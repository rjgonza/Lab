use std::fs::File;

fn main() {
    // let v = vec![0, 1, 2, 3];
    // println!("{}", v[6]);

    let fruits = vec!["banana", "apple", "coconut"];
    let first: Option<&&str> = fruits.get(0);
    println!("{:?}", first);
    let third: Option<&&str> = fruits.get(2);
    println!("{:?}", third);
    let non_existent = fruits.get(100);
    println!("{:?}", non_existent);

    // let f = File::open("hello.txt").unwrap();
    let f = File::open("hello.txt").expect("Failed to open the file");

    // let f = match f {
    //     Ok(file) => file,
    //     Err(error) => panic!("Can't open the file: {:?}", error),
    // };
}
