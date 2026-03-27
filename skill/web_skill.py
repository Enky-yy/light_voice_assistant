import webbrowser

def open_youtube(text=None):
    webbrowser.open("https://youtube.com")
    return "Opening YouTube"


def search_google(text):
    query = text.replace("search", "").strip()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Searching for {query}"