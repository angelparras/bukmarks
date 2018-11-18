import bukmarks as bm


def init():
    chrome = bm.load('chrome.html')
    firefox = bm.load('firefox.html')
    all = chrome + firefox
    bookmarks = bm.parse_links(all)


init()
