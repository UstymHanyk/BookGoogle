# BookGoogle

## Description: 
**<a href="">BookGoogle</a>** is a website aimed at making it easier for its users to choose books.

It provides its user with the following functionality:
1) Searching books by title.
2) Showing the rating and other characteristics of books.
3) Providing the most useful reviews for the book. 

The usefulness is determined by the analysis of the reviews and calculating the amount of neutral vocabulary.

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
    <li><a href="#-usage">Usage</a></li>
    <li><a href="#memo-contributing">Contributing</a></li>
    <li><a href="#busts_in_silhouette-credits">Credits</a></li>
    <li><a href="#closed_lock_with_key-license">License</a></li>
  </ol>
</details>

## Implementation

The following technologies were used to develop the system:
1) Python 3.9
2) HTML, CSS, JS

The backend of the website is taking advantage of the following cloud services:
1) GoodReads API - for retrieving text book reviews from GoodReads website.
2) YouTube Data API v3 - for retrieving links to video book reviews.

The backend also makes use of the following non-standard Python libraries:
1) **nltk** - natural language toolkit.
2) **langdetect** - language-detection library.
3) **flask** - micro web framework.
4) **requests** - convenient library for sending and HTTP requests.

The approximate description of the client-server communication is as follows:
1) The server receives the title of the book from the client.
2) The server gets information about the book with the most similar title using **GoodReads API**.
3) The server retrieves the reviews of the book using **GoodReads API**.
4) The server determines the language of each retrieved review using **langdetect** . 
5) The server measures the neutrality of each English review using **nltk** library.
6) The server selects the reviews with the most emotionally neutral vocabulary.
7) The server retrieves the link to the review of the book using **YouTube Data API v3**.
8) The server sends the response to the client's request. The response contains information about the book, most useful reviews and link to the video book review on YouTube.

## 💻 Usage: 

1) Visit <a href="">www.bookgoogle.com</a>
<br />
<div style="font-size:20px">or</div>

1) Clone this repository with ```git clone https://github.com/UstymHanyk/BookGoogle.git```
2) Install the needed dependecies with ```pip isntall -r requirements.txt```
3) To run the server locally, type the following commands in your terminal:
```bash
$ export FLASK_APP=app.py
$ python -m flask run
```

## :memo: Contributing: 

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## :busts_in_silhouette: Credits: 

Thanks goes to these wonderful people 🚧:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
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

Every developer is welcome to contribute to this project (see <a href="#memo-contributing">Contributing</a>).

## :closed_lock_with_key: License:  
[MIT](https://choosealicense.com/licenses/mit/)