from typing import Union

import dask
import requests
from bs4 import BeautifulSoup

from review_list import ReviewList, Review


def add_page_to_reviews(isbn: Union[str, int], reviews, page: Union[str, int]):
    REVIEWS_URL = f"https://www.goodreads.com/api/reviews_widget_iframe?did=0&format=html&" \
                f"hide_last_page=true&isbn={isbn}&links=660&min_rating=&page={page}&review_back=fff&stars=000&text=000"

    soup = BeautifulSoup(requests.get(url=REVIEWS_URL).text, 'html.parser')

    for review_div in soup.find_all('div', {"class":"gr_review_container"}):
        # print(review_div.find_all("span", {"class":"gr_review_text"}))
        name = review_div.find("span", {"class":"gr_review_by"}).a.text
        try:
            rating = review_div.find("span", {"class":"gr_rating"}).text.count("★")
        except AttributeError:
            continue
        text = review_div.find("div", {"class":"gr_review_text"}).text.strip()
        if text.endswith("...more"):
            text = text[:-7].strip()
        reviews.add_review(Review((name, rating, text)))


if __name__ == "__main__":
    reviews = ReviewList()
    tasks = []
    for i in range(4):
        tasks.append(dask.delayed(add_page_to_reviews)("1602701555", reviews, str(i)))

    dask.compute(*tasks)

    print(reviews)
