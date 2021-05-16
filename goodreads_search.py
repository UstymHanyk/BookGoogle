"""
bookreads_example.py
A usage example of Bookreads API.
"""

import xml.etree.ElementTree as ET
# from pprint import pprint
from icecream import ic as pprint
import time

import requests

SEARCH_BOOKS_ENDPOINT = "https://www.goodreads.com/search/index.xml"


def search_book(search_string: str, search_by: str, num_books: str):
    """Return the result of the book search.
    Parameters
    ----------
    search_string: str
        the phrase to search for
    search_by: str
        Should be one of the following: 'title', 'author', 'all'.
        The parameter tells whether to search by title, author or both.

    Returns
    -------
    list of dictionaries
        A list containing dictionaries that contain information about the books.
        The order of the books remains the same as in the original API response.
    """

    querystring = {
        "q": search_string,
        "key": "BdsXBvnvsl28OVnjElMyA",
        "page": 1,
        "search[field]": search_by
    }

    left_to_search = num_books
    books = []
    while left_to_search > 0:
        response = requests.request(method="GET", url=SEARCH_BOOKS_ENDPOINT, params=querystring)
        pprint(response)
        root = ET.fromstring(response.text)
        root = root.find('search')

        if root.find('total-results').text == '0':
            break

        for book in root.find('results'):
            books.append(element_to_dict(book))

        left_to_search = num_books - len(books)
        querystring['page'] += 1

        # time.sleep(1.2)

    return books[:num_books]

def get_book_isbn(goodreads_id):
    response = requests.request(method="GET", url=f"https://www.goodreads.com/book/show/{goodreads_id}.xml?key=BdsXBvnvsl28OVnjElMyA")
    print(f"https://www.goodreads.com/book/show/{goodreads_id}.xml?key=BdsXBvnvsl28OVnjElMyA")
    pprint('got isbn:',response)
    isbn = ET.fromstring(response.text).find('book').find('isbn')
    return isbn.text



def element_to_dict(element: ET.Element) -> dict:
    """Convert XML root to dictionary with possibly many inner dictionaries.
    The keys of the dictionaries are tags of XML elements.
    Note: make sure that elements with the same parent have different tags.
    """
    dictionary = {}
    for child in element:
        dictionary[child.tag] = element_to_dict(child)
    if any(True for _ in element):
        return dictionary
    return element.text


if __name__ == "__main__":
    res = search_book("12 rules for life", "title", 1)
    for book in res:
        pprint(book)

    pprint(get_book_isbn("40121378"))
    # pprint(get_book_isbn("62221762"))
