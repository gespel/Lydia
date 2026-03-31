use ssh2::Session;
use std::net::TcpStream;

fn check_ssh_login(host: &str, port: u16, username: &str, password: &str) -> bool {
    let tcp = TcpStream::connect((host, port)).map_err(|e| format!("TCP connection failed: {}", e));

    match tcp {
        Ok(tcp) => {
            let mut sess = Session::new().expect("Failed to create SSH session");

            sess.set_tcp_stream(tcp);
            sess.handshake().map_err(|e| format!("SSH handshake failed: {}", e)).expect("SSH handshake failed!");

            match sess.userauth_password(username, password) {
                Ok(_) => {
                    sess.authenticated()
                },
                Err(_) => false,
            }
        },
        Err(_) => {
            println!("Unable to connect to target!");
            false
        }
    }
}

fn main() {
    let result = check_ssh_login("", 22, "", "");

    match result {
        true => {
            println!("Login successful!");
        },
        false => {
            println!("Login failed.");
        }
    }
}
