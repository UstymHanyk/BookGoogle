"""
Module contains class 'Review', which contains information
about book review, written in english, and class 'ReviewList',
which keeps all book reviews.
"""

from nltk.sentiment import SentimentIntensityAnalyzer
import time
from typing import List

class Review:
    """Review information"""
    def __init__(self, info_tuple: tuple):
        """Initializes the class."""
        self.author = info_tuple[0]
        self.rating = info_tuple[1]
        self.text = info_tuple[2]
        self.length = len(info_tuple[2])
        self.neutrality = self.calc_neutrality()

    def calc_neutrality(self) -> float:
        """Calculates the text neutrality."""
        sia_object = SentimentIntensityAnalyzer()
        return sia_object.polarity_scores(self.text)['neu']

    def __lt__(self, other) -> bool:
        """Compares reviews reliability."""
        if self.rating == other.rating:
            if self.neutrality == other.neutrality:
                if self.length < other.length:
                    return True
                else:
                    return False
            return self.neutrality < other.neutrality
        return self.rating < other.rating

    def __repr__(self) -> str:
        """
        Returns the string to represent the
        class.
        """
        return f"username: {self.author}\nrating: \
{self.rating*'⋆'}\n{self.text}\ntotal length: {self.length}\n\
neutrality of text: {self.neutrality}\n"

class ReviewList:
    """Keeps and sort Review objects."""
    def __init__(self):
        """Initialize the class."""
        self.reviews = []

    def __repr__(self) -> str:
        """
        Returns the string to represent the
        class.
        """
        final_str = ''
        for review in self.reviews:
            final_str += str(review)
        return final_str

    def add_review(self, review: Review):
        """Adds a new review."""
        self.reviews.append(review)

    def reliability_sort(self):
        """
        Sorts reviews by their rates, length and
        number of neutral lexicon.
        """
        self.reviews.sort(reverse=True)

    def get_mood_range(self) -> List[Review]:
        """
        Returns the list of three most reliable
        reviews from the all given.
        """
        result = []
        mood_set = [5, 3, 2]
        index = 0
        while index < 3:
            for review in self.reviews:
                if index < 3:
                    if review.rating == mood_set[index]:
                        result.append(review)
                        index += 1
            index += 1
        return result
