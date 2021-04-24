import requests
from bs4 import BeautifulSoup, SoupStrainer

def scrape_reviews(isbn):
    """
    Scrape reviews from book's Goodreads webpage using BeautifulSoup 4.
    Return a list of tuples (names,rating,reviews)
    """
    requests_session = requests.Session()  # Launch a requests session in order to improve performance

    book_page_url = f"https://www.goodreads.com/api/reviews_widget_iframe?did=0&format=html&" \
                    f"hide_last_page=true&isbn={isbn}&links=660&min_rating=&page=2&review_back=fff&stars=000&text=000"
    webpage = requests_session.get(book_page_url)

    soup = BeautifulSoup(webpage.content, "lxml")
    # reviews_raw = soup.find_all('div', class_='gr_review_text')
    # reviews = [review.text.strip() for review in reviews_raw]

    names_raw = soup.find_all('a', itemprop="discussionUrl")  # find names of the review authors
    names = [name.text for name in names_raw]
    print(names)
    ratings_raw = soup.find_all('span', class_="gr_rating")  # find ratings of the review
    ratings = [rating.text.count("★") for rating in ratings_raw]  # convert starred rating into integer value
    print(ratings)

    reviews = []
    full_review_links = soup.find_all('link',itemprop="url")  # find links to the full reviews
    only_review_tags = SoupStrainer(itemprop="reviewBody")  # use special bs4 object to load the webpage partially
    for full_review_link in full_review_links:
        full_review_webpage = requests_session.get(full_review_link.attrs["href"])
        soup = BeautifulSoup(full_review_webpage.content, "lxml", parse_only=only_review_tags)
        review_raw_text = soup.find('div', class_="reviewText")  # find full text of the review
        reviews.append(review_raw_text.text.strip())  # add review text to the reviews list

    full_reviews = list(zip(names, ratings, reviews)) # make a list of tuples containing full info about reviews
    return full_reviews

print(scrape_reviews(9780596002817))
