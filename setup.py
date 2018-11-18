import bukmarks as bm


def init():
    already_imported = bm.load('bookmarks.csv')
    chrome = bm.import_file('chrome.html')
    firefox = bm.import_file('firefox.html')
    all = chrome + firefox
    bm.parse_links(all, already_imported)

init()