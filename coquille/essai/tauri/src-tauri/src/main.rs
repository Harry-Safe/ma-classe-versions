// Sans fenêtre de console sous Windows (version publiée).
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

fn main() {
    glacis_lib::run()
}
