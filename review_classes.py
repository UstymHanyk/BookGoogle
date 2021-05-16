"""
Module contains class 'Review', which contains information
about book review, written in english, and class 'ReviewList',
which keeps all book reviews.
"""

from nltk.sentiment import SentimentIntensityAnalyzer
from typing import List
from langdetect import detect


class Review:
    """Information about the review."""

    def __init__(self, info_tuple: tuple):
        """Initializes the class."""
        self.author = info_tuple[0]
        self.rating = info_tuple[1]
        self.text = info_tuple[2]
        self.length = len(info_tuple[2])
        self.neutrality = self.calc_neutrality()

    def calc_neutrality(self) -> float:
        """Calculates neutral lexic's percentage
        in the text."""
        sia_object = SentimentIntensityAnalyzer()
        return sia_object.polarity_scores(self.text)['neu']

    def __lt__(self, other) -> bool:
        """Compares reviews' ratings and reliability
        by three aspects.
        1 - rating
        2 - amount of neutral language
        3 - length of the text
        Method is needed for future comparing of reviews
        and sorting."""
        if self.rating == other.rating:
            if self.neutrality == other.neutrality:
                if self.length < other.length:
                    return True
                else:
                    return False
            return self.neutrality < other.neutrality
        return self.rating < other.rating

    def __repr__(self) -> str:
        """Returns the string to represent the
        class."""
        return f"username: {self.author}\nrating: \
{self.rating * '⋆'}\n{self.text}\ntotal length: {self.length}\n\
neutrality of text: {self.neutrality}\n"


class ReviewList:
    """Keeps and sort Review objects."""

    def __init__(self):
        """Initializes the class."""
        self.reviews = []

    def __repr__(self) -> str:
        """Returns the string to represent the
        class."""
        final_str = ''
        for review in self.reviews:
            final_str += str(review)
        return final_str

    def clear(self):
        """
        Clears itself and returns all of the data
        """
        deleted_data = ReviewList()
        deleted_data.reviews = self.reviews
        self.reviews = []
        return deleted_data

    def add_review(self, review: Review):
        """Adds a new review if it's written in English."""
        if not review.text.split('.')[0].isdigit():
            if detect(review.text.split('.')[0]) == 'en':
                self.reviews.append(review)

    def reliability_sort(self):
        """Sorts reviews by their rates, length and
        number of neutral language in descending order.
        Here the adapted method __lt__ for class
        Reviews is used."""
        self.reviews.sort(reverse=True)

    def get_mood_range(self, mood_lst=[5, 3, 2]) -> List[Review]:
        """
        Returns the list of three most reliable
        reviews from the all given.

        Gets the sorted list of reviews and returns
        list with first positive, nutral and negative reviews
        (rating 5, 3 and 2 in accordance). There would be our
        most reliable reviews from every category.

        If there are no reviews with ratings5 or 2, the method
        will return reviews with ratings 4 or 1.
        """
        result = []
        index = 0

        while index < len(mood_lst):
            for review in self.reviews:
                if index < len(mood_lst):
                    if review.rating == mood_lst[index]:
                        result.append(review)
                        index += 1
            index += 1

        if len(result) < 3 and len(mood_lst) > 2:
            if any(review.rating == 2 for review in result) is False and \
                    any(review.rating == 5 for review in result) is False:
                # self.get_mood_range(mood_lst=[4, 1])
                result += self.get_mood_range(mood_lst=[4, 1])
                # result += self.get_mood_range(mood_lst=[4])
            elif not any(review.rating == 5 for review in result):
                result += self.get_mood_range(mood_lst=[4])
            elif not any(review.rating == 2 for review in result):
                result += self.get_mood_range(mood_lst=(1,))
            result.sort(reverse=True)
        return result

# txt='3.5 StarsI like the can-do attitude Vance took with hounding Musk and wearing him down till he agreed to cooperate with this biography. I also appreciated all the "Holy crap, Musk is CRAZY. CRAZY like a fox," moments I had while reading this. The only thing that keeps this from being a 4-star book is that the reporting and writing leans too heavily on idolatry. There were passages where I literally cringed at how much of a fanboy Vance sounded like.'
# rv=ReviewList()
# review= Review(("MAx",'4',txt))
# rv.add_review(review)
# print(rv.reviews)