import csv
import urllib.error as error
import urllib.request as urllib
from datetime import date
from http import client


from lxml.html import fromstring


def parse_links(html: str, ignore: list) -> dict:
    """
    Parse links info from bookmarks file
    :param html:
    :return: dict
    """
    parser: object = fromstring(html)
    links: dict = enumerate(parser.xpath('//dt/a'))
    ok = {}
    for i, v in links:
        href: str = v.get('href')
        add_date: int = int(v.get('add_date'))
        name: str = str(v.text)
        if href not in ignore:
            extract({
                'name': name,
                'href': href,
                'add_date': date.fromtimestamp(add_date),
                'exists': exist(href)
            })


def extract(parsed: dict, type: str = 'csv') -> dict:
    """
    Save bookmarks list to csv format
    :param parsed:
    :return: dict
    """
    if type == 'csv':
        save('bookmarks.csv', parsed)


def exist(url: object) -> bool:
    """
    Check if url exists (response code)
    :param url:
    :return:
    """
    request: object = urllib.Request(url)
    request.add_header('User-agent',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0')
    try:
        resp: object = urllib.urlopen(request, timeout=5)
        code: int = resp.getcode()
        if code >= 400:
            return 'NO'
    except (error.URLError, error.HTTPError, error.ContentTooShortError, client.HTTPException, TimeoutError) as e:
        return 'FAILED'
    return 'YES'


def save(filename: str, bookmarks: dict) -> None:
    """
    Saves dictionary to CSV file
    :param filename:
    :param bookmarks:
    :return: None
    """
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames: list = ['name', 'href', 'add_date', 'exists']
        writer: object = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writerow(bookmarks)

def load(filename: str) -> list:
    """
    Return links present in CSV file
    :param filename:
    :return: list
    """
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            fieldnames: list = ['name', 'href', 'add_date', 'exists']
            reader: object = csv.DictReader(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            already: list = []
            for row in reader:
                already.append(row['href'])
            return already
    except:
        return []



def import_file(filename: str) -> str:
    """
    Load file into string
    :param filename: 
    :return: 
    """
    with open(filename, 'r') as f:
        data = f.read()
        return data
