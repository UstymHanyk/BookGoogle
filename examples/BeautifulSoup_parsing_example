import requests
from bs4 import BeautifulSoup


def scrape_reviews(isbn):
    """
    Scrape reviews from book's Goodreads webpage using BeautifulSoup 4.
    Return a list of tuples (names,rating,reviews)
    """

    book_page_url = f"https://www.goodreads.com/api/reviews_widget_iframe?did=0&format=html&hide_last_page" \
                    f"=true&isbn={isbn}&links=660&min_rating=&page=2&review_back=fff&stars=000&text=000"
    webpage = requests.get(book_page_url)
    soup = BeautifulSoup(webpage.content, "html.parser")

    reviews_raw = soup.find_all('div', class_='gr_review_text')  # find containers containing text of the review
    reviews = [review.text.strip() for review in reviews_raw]  # delete unnecessary whitespace
    names_raw = soup.find_all('a', itemprop="discussionUrl")  # find names of the review authors
    names = [name.text for name in names_raw]
    ratings_raw = soup.find_all('span', class_="gr_rating")  # find ratings of the review
    ratings = [rating.text.count("★") for rating in ratings_raw]  # convert starred rating into integer value

    full_reviews = list(zip(names, ratings, reviews))  # make a list of tuples containing full info about reviews
    return full_reviews


print(scrape_reviews(9780596002817))
