import os

def open_vscode(text=None):
    os.system("code")
    return "Opening VS Code"


def shutdown(text=None):
    os.system("shutdown now")  # ⚠️ Linux only
    return "Shutting down system"


def open_app(text):
    if "code" in text:
        return open_vscode()

    return "App not recognized"