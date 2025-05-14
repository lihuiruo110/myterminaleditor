import { Terminal } from "https://cdn.jsdelivr.net/npm/xterm@5.3.0/+esm";

def create_terminal(container):
    term = Terminal()
    term.open(container)
    term.write("Welcome to your terminal\r\n")
    return term
