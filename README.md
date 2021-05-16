# BookGoogle

## Description: 
**<a href="">BookGoogle</a>** is a website aimed at making it easier for its users to decide on what book to read.

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
    <li><a href="#wrench-implementation">Implementation</a></li>
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

### Approximate algorithm
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
The following is a tree representing the project structure with all important files:
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
    │   ├───search_book() function - return info about books found by searching
    │   ├───get_book_isbn() helper function - return ISBN of the book given its GoodReads id
    │   └───element_to_dict() helper function - converts xml.etree.ElementTree.Element to the dictionary of dictionaries
    ├───static
    │   └───styles - a folder with css styles
    │       ...
    └───templates - HTML templates
        ├───book.html
        ├───index.html
        └───layout.html
```

## 💻 Usage: 

1) Visit <a href="">www.bookgoogle.com</a>

**or**

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