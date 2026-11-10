// Sans fenêtre de console sous Windows (version publiée).
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

fn main() {
    ma_classe_lib::run()
}
