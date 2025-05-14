import CodeMirror from "https://cdn.jsdelivr.net/npm/codemirror@5.65.2/lib/codemirror.js";

def create_editor(container):
    editor = CodeMirror(container, {
        lineNumbers: True,
        mode: "javascript",
    })
    return editor
