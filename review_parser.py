import requests
from bs4 import BeautifulSoup, SoupStrainer
import dask
from review_classes import ReviewList, Review
from time import time
from requests_futures.sessions import FuturesSession

# requests_session = requests.Session()
requests_session = FuturesSession()
@dask.delayed
def find_full_review_text(url, iteration):
    only_review_tags = SoupStrainer(itemprop="reviewBody")  # use special bs4 object to load the webpage partially
    start_time = time()
    full_review_webpage = requests_session.get(url.attrs["href"])
    # full_review_webpage = requests.get(url.attrs["href"])

    if time() - start_time > 3:
        print(f"---{iteration} overtime --- {time() - start_time:.2f} seconds to make 1 request {url.attrs['href']}")
    print(f"---{iteration} {time()-start_time:.2f} seconds to make 1 request {url.attrs['href']}")

    soup = BeautifulSoup(full_review_webpage.result().content, "html.parser", parse_only=only_review_tags)
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
    start_review_page_scrape = time()
    webpage = requests_session.get(book_page_url).result()
    # webpage = requests.get(book_page_url)
    if webpage.status_code == 404:
        return
    soup = BeautifulSoup(webpage.content, "html.parser")
    names_raw = soup.find_all('a', itemprop="discussionUrl")  # find names of the review authors
    names = [name.text for name in names_raw]

    ratings_raw = soup.find_all('span', class_="gr_rating")  # find ratings of the review
    ratings = [rating.text.count("★") for rating in ratings_raw]  # convert starred rating into integer value

    full_review_texts = []
    full_review_links = soup.find_all('link',itemprop="url")  # find links to the full reviews

    iteration = 0
    for full_review_link in full_review_links:
        full_review_texts.append(find_full_review_text(full_review_link,iteration/10 + page))
        iteration +=1
    print(f"-Finished page({page}) surface scraping in {time() - start_review_page_scrape:.2f}")

    start_computing=time()
    computed_reviews = zip(names, ratings, dask.compute(*full_review_texts))
    print(f"--Finished {page} full text computing in {time() - start_computing:.2f}")

    # start_adding_time = time()
    for review_tuple in computed_reviews:
        reviews.add_review(Review(review_tuple))
    # print(f"Added reviews(page {page}) to the ReviewList in {time() - start_adding_time:.2f}")

def scrape_reviews(isbn):
    """
    Scrapes 4 pages of reviews from Goodreads using scrape_reviews_helper().

    In order to increase performance the multitasking module dask is used, which
    helps speed up the process by 1000%.
    After scraping the global(globality is necessary due to the intricacies of dask) variable reviews is cleared.
    """

    to_be_computed = [scrape_reviews_helper(isbn,page) for page in range(1,12)]
    print("reviews are collected")
    dask.compute(*to_be_computed)
    # print(len(reviews.reviews))
    return reviews.clear()

# print(scrape_reviews('0140449337'))
