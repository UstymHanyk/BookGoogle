from flask import Flask, render_template, request

from goodreads_search import search_book, get_book_isbn
from review_parser import scrape_reviews
from youtube_search import get_video_ids
# from icecream import ic as pprint
from pprint import pprint
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/book_info", methods=["POST"])
def show_book_info_page():
    book_title = request.form["book_title"]
    book_dict = search_book(book_title, "title", 1)[0]

    # enlarging the image(which is initially low-quality) by editing its url
    book_cover_url = book_dict["best_book"]["image_url"][:-7] + "318_.jpg" if book_dict["best_book"]["image_url"][
                                                            -5] == "_" else book_dict["best_book"]["image_url"]

    book_cover_url = f"background-image:url('{book_cover_url}');"

    book_isbn = get_book_isbn(book_dict["best_book"]["id"])
    pprint(book_isbn)

    reviews = scrape_reviews(book_isbn).get_mood_range()

    youtube_video_id = get_video_ids(book_dict["best_book"]["title"] + " book review",1)[0]
    # pprint(reviews)
    return render_template("book.html", book_dict=book_dict, reviews=reviews, book_cover_url=book_cover_url,
                           youtube_video_id = youtube_video_id)


# enter the code below to launch the web server
# FLASK_APP=app.py FLASK_ENV=development flask run
