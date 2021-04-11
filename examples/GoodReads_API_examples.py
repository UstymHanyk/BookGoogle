from goodreads import client

client = client.GoodreadsClient('BdsXBvnvsl28OVnjElMyA', '')
#__________WORK WITH BOOKS____________

# Access the first book added to Goodread. It is the book with id 1.
book = client.book(1)
book_author = book.authors # Access to author of the book.

print(book.title) # Displays the title of the book.
print(book.average_rating) # Displays the average rating of the book
print(book_author[0].name) # Displays author's name.

# _________WORK WITH AUTHOR_____________

# get information about an author by his ID
author = client.author(2617)
print(author.name) # Displays the author's name.
print(author.works_count) # Displays the author's number of books.
print(author.books) # Displays the author's books.

# _________WORK WITH USER_____________

# get information about a user by his ID
user = client.user(1)
print(user.name) # Displays the user's name.
print(user.user_name) # Displays user name.
print(user.owned_books) # Displays owned books.