struct Film {
    title: String,
    director: String,
    studio: String,
}

struct Book {
    title: String,
    author: String,
    publisher: String,
}

struct Album {
    title: String,
    artist: String,
    label: String,
}

trait Catalog {
    fn describe(&self) {
        println!("We need more information about this type of media!");
    }
}

impl Catalog for Film {
    fn describe(&self) {
        println!(
            "{} was directed by {} through {} studios",
            self.title, self.director, self.studio
        )
    }
}

impl Catalog for Book {
    fn describe(&self) {
        println!(
            "{} was written by {} and published by {}",
            self.title, self.author, self.publisher
        )
    }
}

impl Catalog for Album {}

fn main() {
    let capt_marvel = Film {
        title: String::from("Captain Marvel"),
        director: String::from("Anna Boden and Ryan Fleck"),
        studio: String::from("Marvel"),
    };

    capt_marvel.describe();

    let elantris = Book {
        title: String::from("Elantris"),
        author: String::from("Barndon Sanderson"),
        publisher: String::from("Tor Books"),
    };

    elantris.describe();

    let let_it_be = Album {
        title: String::from("Let it Be"),
        artist: String::from("The Beatles"),
        label: String::from("Apple"),
    };

    let_it_be.describe();
}
