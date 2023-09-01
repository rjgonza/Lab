use std::io::{stderr, Write};
use std::env;
use std::process::exit;


fn main() {
    let mut students = vec![Student {
        name: "Ryan".to_string(),
    }];

    students.push(Student {
        name: "Lisa".to_string(),
    });

    assert!(
        &students[0]
            == &Student {
                name: "Ryan".to_string()
            }
    );

    assert!(
        students.get(0)
            == Some(&Student {
                name: "Ryan".to_string()
            })
    );

    assert!(students.get(100000) == None);

    for student in students.iter() {
        println!("Student name: {}", student.name);
    }

    use std::collections::HashMap;
    let mut enrollment = HashMap::new();
    enrollment.insert("biology".to_string(), students);

    let bio_students = enextern crate ssl_expiration;

use std::io::{stderr, Write};
use std::env;
use std::process::exit;

fn main() {
    let mut exit_code = 0;
    for domain in env::args().skip(1) {
        match ssl_expiration::SslExpiration::from_domain_name(&domain) {
            Ok(expiration) => {
                let days = expiration.days();
                if expiration.is_expired() {
                    let _ = writeln!(stderr(),
                                     "{} SSL certificate expired {} days ago",
                                     domain,
                                     !days);
                    exit_code = 1;
                } else {
                    println!("{} SSL certificate will expire in {} days", domain, days);
                }
            }
            Err(e) => {
                let _ = writeln!(stderr(),
                                 "An error occured when checking {}: {}",
                                 domain,
                                 e.description());
            }
        }
    }
    exit(exit_code);
}rollment.get("biology");
    let students = enrollment.remove("biology");
}

#[derive(PartialEq, Eq)]
struct Student {
    name: String,
}

fn main() {
    let mut exit_code = 0;
    for domain in env::args().skip(1) {
        match ssl_expiration::SslExpiration::from_domain_name(&domain) {
            Ok(expiration) => {
                let days = expiration.days();
                if expiration.is_expired() {
                    let _ = writeln!(stderr(),
                                     "{} SSL certificate expired {} days ago",
                                     domain,
                                     !days);
                    exit_code = 1;
                } else {
                    println!("{} SSL certificate will expire in {} days", domain, days);
                }
            }
            Err(e) => {
                let _ = writeln!(stderr(),
                                 "An error occured when checking {}: {}",
                                 domain,
                                 e.description());
            }
        }
    }
    exit(exit_code);
}