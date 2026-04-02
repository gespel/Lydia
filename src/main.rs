use ssh2::Session;
use std::net::TcpStream;
use colored::Colorize;
use std::io::Write;
use chrono::Local;
use env_logger::Builder;
use log::LevelFilter;

fn check_ssh_login(host: &str, port: u16, username: &str, password: &str) -> bool {
    let tcp = TcpStream::connect((host, port)).map_err(|e| format!("TCP connection failed: {}", e));

    match tcp {
        Ok(tcp) => {
            let mut sess = Session::new().expect("Failed to create SSH session");

            sess.set_tcp_stream(tcp);
            sess.handshake().map_err(|e| format!("SSH handshake failed: {}", e)).expect("SSH handshake failed!");

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
            println!("Unable to connect to target! {:?}", e);
            false
        }
    }
}

fn main() {
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

    check_ssh_login("127.0.0.1", 2222, "root", "passworda");
    check_ssh_login("127.0.0.1", 2222, "root", "password");

}
