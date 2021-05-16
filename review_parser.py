import requests
from bs4 import BeautifulSoup, SoupStrainer
import dask
from review_classes import ReviewList, Review

requests_session = requests.Session()
@dask.delayed
def find_full_review_text(url):
    only_review_tags = SoupStrainer(itemprop="reviewBody")  # use special bs4 object to load the webpage partially
    full_review_webpage = requests_session.get(url.attrs["href"])
    soup = BeautifulSoup(full_review_webpage.content, "html.parser", parse_only=only_review_tags)
    review_raw_text = soup.find('div', class_="reviewText")  # find full text of the review
    if not review_raw_text:
        return "Error! Review text not found"
    return review_raw_text.text.strip()  # add review text to the reviews list

reviews = ReviewList()

@dask.delayed
def scrape_reviews_helper(isbn, page):
    """
    Scrape reviews from book's Goodreads webpage using BeautifulSoup 4.
    Return a list of tuples (names,rating,reviews)
    """
    book_page_url = f"https://www.goodreads.com/api/reviews_widget_iframe?did=0&format=html&" \
                    f"hide_last_page=true&isbn={isbn}&links=660&min_rating=&page={page}&review_back=fff&stars=000&text=000"
    print(book_page_url)
    webpage = requests_session.get(book_page_url)
    if webpage.status_code == 404:
        return
    soup = BeautifulSoup(webpage.content, "html.parser")
    names_raw = soup.find_all('a', itemprop="discussionUrl")  # find names of the review authors
    names = [name.text for name in names_raw]

    ratings_raw = soup.find_all('span', class_="gr_rating")  # find ratings of the review
    ratings = [rating.text.count("★") for rating in ratings_raw]  # convert starred rating into integer value

    full_review_texts = []
    full_review_links = soup.find_all('link',itemprop="url")  # find links to the full reviews
    for full_review_link in full_review_links:
        full_review_texts.append(find_full_review_text(full_review_link))
    computed_reviews = zip(names, ratings, dask.compute(*full_review_texts))

    for review_tuple in computed_reviews:
        reviews.add_review(Review(review_tuple))

def scrape_reviews(isbn):
    """
    Scrapes 4 pages of reviews from Goodreads using scrape_reviews_helper().

    In order to increase performance the multitasking module dask is used, which
    helps speed up the process by 1000%.
    After scraping the global(globality is necessary due to the intricacies of dask) variable reviews is cleared.
    """


    to_be_computed = [scrape_reviews_helper(isbn,page) for page in range(1,4)]

    dask.compute(*to_be_computed)
    # print(len(reviews.reviews))
    return reviews.clear()

# print(scrape_reviews('0345816021').reviews)
