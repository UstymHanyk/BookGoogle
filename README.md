# BookGoogle

## Description: 
**<a href="https://book-google-app.herokuapp.com/">BookGoogle</a>** is a website aimed at making it easier for its users to decide on what book to read.

It provides its user with the following functionality:
1) Searching books by title.
2) Showing the rating and other characteristics of books.
3) Providing the most useful reviews for the book. 

The usefulness is determined by the analysis of the reviews and calculating the amount of emotionally neutral vocabulary.

## :bookmark_tabs: Table of Contents:
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#description">Description</a>
    </li>
    <li>
      <a href="#bookmark_tabs-table-of-contents">Table of Contents</a>
    </li>
    <li>
      <a href="#wrench-implementation">Implementation</a>
      <ul>
        <li><a href="#used-technologies">Used technologies</a></li>
        <li><a href="#algorithm">Algorithm</a></li>
        <li><a href="#project-structure">Project structure</a></li>
      </ul>
    </li>
    <li><a href="#-usage">Usage</a></li>
    <li><a href="#memo-contributing">Contributing</a></li>
    <li><a href="#busts_in_silhouette-credits">Credits</a></li>
    <li><a href="#closed_lock_with_key-license">License</a></li>
  </ol>
</details>

## :wrench: Implementation
### Used technologies
The following technologies were used to develop the system:
1) Python 3.9
2) HTML, CSS

The backend of the website takes advantage of the following cloud services:
1) **GoodReads API** - for retrieving text book reviews from GoodReads website.
2) **YouTube Data API v3** - for retrieving links to video book reviews.

The backend also makes use of the following non-standard Python libraries:
1) **nltk** - natural language toolkit.
2) **langdetect** - language-detection library.
3) **flask** - micro web framework.
4) **requests** - convenient library for sending HTTP requests.
5) **dask** - library for parallel computing.

### Algorithm
The approximate description of the client-server communication is as follows:
1) The server receives the title of the book from the client.
2) The server gets information about the book with the most similar title using **GoodReads API**.
3) The server retrieves the reviews of the book using **GoodReads API**.
4) The server determines the language of each retrieved review using **langdetect** library. 
5) The server measures the neutrality of each English review using **nltk** library.
6) The server selects the reviews with the most emotionally neutral vocabulary.
7) The server retrieves the link to the video review of the book using **YouTube Data API v3**.
8) The server sends the response to the client's request. The response contains the information about the book, most useful reviews and the link to the video book review on YouTube.

### Project structure
The following is a tree representing the project structure with all the important files:
```
└───root directory
    ├───app.py - main file of the web aplication linking all routes to python code
    │   ├───index() function - provides "/" endpoint for main page
    │   └───show_book_info_page() function - provides "/book_info" endpoint for receiving page with info about boook
    ├───review_classes.py - provides the implementation of ReviewList ADT
    │   ├───class Review
    │   └───class ReviewList
    ├───review_parser.py - provides functions for retrieving book reviews by scraping GoodReads, utilizes ReviewList ADT
    │   ├───scrape_reviews() function - return reviews of the book given its ISBN
    │   ... - some other helper methods
    ├───goodreads_search.py - provides book search
    │   ├───search_book() function - return info about books found
    │   ├───get_book_isbn() helper function - return ISBN of the book given its GoodReads ID
    │   └───element_to_dict() helper function - converts xml.etree.ElementTree.Element to the dictionary of dictionaries
    ├───youtube_search.py
    │   ├───get_video_ids() function - return list of IDs of YouTube videos from search query.
    │   ├───get_video_info() function - return information on the video given its ID.
    ├───test_review_classes.py - module for testing class Review and class ReviewList.
    │   └───class TestReviews
    ├───static
    │   └───styles - a folder with css styles
    │       ...
    └───templates - HTML templates
        ├───book.html
        ├───index.html
        └───layout.html
```

Class **ReviewList** is a container for instances of **Review** class.

Class **Review** represents a review with associated text, rating, name of author and calculated level of neutrality. The instances of Review can be compared (<, => etc.) with each other. The following methods are implemented in Review:
* \_\_init__(self, info_tuple) - creates instance of Review from passed in tuple containing the name of the author, the rating and the text of the review.
* calc_neutrality(self) - calculate and return the level of neutrality of the review.
* \_\_lt__(self, other) - compare two reviews. If the ratings are equal, the one with the greater level of neutrality is greater. We suppose that greater neutrality corresponds to the greater reliability.
* \_\_repr__(self) - return text represetation of the review.

Class **ReviewList** is an implemantation of the ReviewList ADT. It is designed to contain and sort by reliability the instances of Review.
The class has the following methods:
* \_\_init__(self) - create ReviewList
* \_\_repr__(self) - return text representation of ReviewList
* clear(self) - clears itself and returns all of the data
* add_review(self, review) - add Review object to ReviewList
* reliability_sort() - sort the interal list of reviews
* get_mood_range(self, mood_lst) - return the most reliable (with the most emotionally neutral vocabulary) reviews that have ratings from mood_lst.

Class **TestReviews** in test_review_classes.py is a unittest testcase. It is designed to test class Review and class ReviewList from review_classes.py. The TestReviews class has the following methods:
* setUp(self) - create isntances of Review for futher testing in each test example.
* test_correct_review(self) - test the correctness of attributes of reviews.
* test_reviews_compare(self) - test the order of the instances of Review (>, <= etc.).
* test_add_review_list(self) - test adding reviews to the instance of ReviewList.
* test_review_list_sorting1(self) - test extracting the most neutral reviews from ReviewList.
* test_review_list_sorting2(self) - test extracting the most neutral reviews from ReviewList.
* test_review_list_sorting3(self) - test extracting the most neutral reviews from ReviewList.

## 💻 Usage: 
### Our website
1) Visit <a href="https://book-google-app.herokuapp.com/">book-google-app.herokuapp.com/</a>

<img src="https://raw.githubusercontent.com/UstymHanyk/BookGoogle/main/images/website1.png" />

2) Enter the title of the book and press Enter.

<img src="https://raw.githubusercontent.com/UstymHanyk/BookGoogle/main/images/website2.png" />

3) Wait till the server gives a response with some information about the book.

<img src="https://raw.githubusercontent.com/UstymHanyk/BookGoogle/main/images/website3.png" />

4) After some time the website will also display the reviews of the book.

<img src="https://raw.githubusercontent.com/UstymHanyk/BookGoogle/main/images/website4.png" />


### Running website locally
Alternatively, you can run the website on the local computer (Python 3.9 is supported):
1) Clone this repository with
```shell
$ git clone https://github.com/UstymHanyk/BookGoogle.git
```
2) Install the needed dependecies with 
```shell
$ pip install -r requirements.txt
```
4) Replace the missing API keys in project files with your own GoodReads API key and Youtube API key.
5) To run the server locally, type the following commands in your terminal:
```shell
$ export FLASK_APP=app.py
$ python -m flask run
```

## :memo: Contributing: 

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## :busts_in_silhouette: Credits: 

The project was developed as a group home assignment within the course "Basics of programming" at UCU by the following people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/UstymHanyk/"><img src="https://avatars.githubusercontent.com/u/25267338?v=4" width="100px;" alt=""/><br /><sub><b>Ustym Hanyk</b></sub></a><br /><a href="https://github.com/UstymHanyk/BookGoogle/commits?author=UstymHanyk" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/sininni"><img src="https://avatars.githubusercontent.com/u/73228110?v=4" width="100px;" alt=""/><br /><sub><b>Nadiia Zaiachkovska</b></sub></a><br /><a href="https://github.com/UstymHanyk/BookGoogle/commits?author=sininni" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/bogdanmagometa"><img src="https://avatars.githubusercontent.com/u/34510991?v=4" width="100px;" alt=""/><br /><sub><b>Bohdan Mahometa</b></sub></a><br /><a href="https://github.com/UstymHanyk/BookGoogle/commits?author=bogdanmagometa" title="Code">💻</a></td>
  </tr>
</table>
<table align="center">
  <tr >
    <td align="center"><a href="https://github.com/DmytroKomarynskyi"><img src="https://avatars.githubusercontent.com/u/80006043?v=4" width="100px;" alt=""/><br /><sub><b>Dmytro Komarynskyi</b></sub></a><br /><a href="https://github.com/UstymHanyk/BookGoogle/commits?author=DmytroKomarynskyi" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/orca-acro"><img src="https://avatars.githubusercontent.com/u/73779109?v=4" width="100px;" alt=""/><br /><sub><b>Daryna Cheban</b></sub></a><br /><a href="https://github.com/UstymHanyk/BookGoogle/commits?author=orca-acro" title="Code">💻</a></td>
  </tr>
</table>
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

Every other developer is welcome to contribute to this project too (see <a href="#memo-contributing">Contributing</a>).

## :closed_lock_with_key: License:  
[MIT](https://choosealicense.com/licenses/mit/)