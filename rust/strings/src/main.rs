fn main() {
    let text = "Hello\nworld\n!";
    let upper = text.to_uppercase();
    let stripped = upper.strip_prefix("HELLO\n").unwrap();
    // println!("{}", first_line(text))
    println!("{}", stripped)
}

// pub fn first_line(string: String) -> String {
pub fn first_line(string: &str) -> &str {
    // string.lines().next().unwrap().to_owned() // copy everything and then return that
    string.lines().next().unwrap()
}
