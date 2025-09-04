def parse(text):
    text = text.lower()
    for keyword in keywords.keys():
        if keyword in text:
            return keywords[keyword]
    return {"action":"unknown","target":"unknown"}

keywords = {
    "browser":{"action":"open_browser","targer":"browser"},
    "music":{"action":"open_spotify","target":"spotify"},
}