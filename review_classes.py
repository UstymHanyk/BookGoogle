"""
Module contains class 'Review', which contains information
about book review, written in english, and class 'ReviewList',
which keeps all book reviews.
"""

from nltk.sentiment import SentimentIntensityAnalyzer
from typing import List
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException


class Review:
    """
    Information about the review.
    """

    def __init__(self, info_tuple):
        """
        Initializes the class.

        :type info_tuple: tuple
        :param info_tuple: Information about the review.
        """
        self.author = info_tuple[0]
        self.rating = info_tuple[1]
        self.text = info_tuple[2]
        self.length = len(info_tuple[2])
        self.neutrality = self.calc_neutrality()

    def calc_neutrality(self):
        """
        Calculates neutral lexic's percentage
        in the text.

        :type output: float
        :param output: Neutrality.
        """
        sia_object = SentimentIntensityAnalyzer()
        return sia_object.polarity_scores(self.text)['neu']

    def __lt__(self, other) -> bool:
        """
        Compares reviews' ratings and reliability
        by three aspects.
        1 - rating
        2 - amount of neutral language
        3 - length of the text
        Method is needed for future comparing of reviews
        and sorting.

        :type other: Review
        :param other: Another review.        
        """
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
    """
    Keeps and sort Review objects.
    """

    def __init__(self):
        """Initializes the class."""
        self.reviews = []

    def __repr__(self) -> str:
        """
        Returns the string to represent the
        class.

        :type output: str
        :param output: Representance of class object.
        """
        final_str = ''
        for review in self.reviews:
            final_str += str(review)
        return final_str

    def clear(self):
        """
        Clears itself and returns all of the data
        
        :type output: ReviewList
        :param output: Copy of object.
        """
        deleted_data = ReviewList()
        deleted_data.reviews = self.reviews
        self.reviews = []
        return deleted_data

    def add_review(self, review):
        """
        Adds a new review if it's written in English.

        :type review: Review
        :param review: New review.
        """
        try:
            if detect(review.text.split('.')[0]) == 'en':
                self.reviews.append(review)
        except LangDetectException:
            print(f"Language of ({review.text.split('.')[0]}) could not be detect")

    def reliability_sort(self):
        """
        Sorts reviews by their rates, length and
        number of neutral language in descending order.
        Here the adapted method __lt__ for class
        Reviews is used.
        """
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

        :type output: List[Review]
        :param output: List of Review objects.        
        """
        self.reliability_sort()
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
                result += self.get_mood_range(mood_lst=[4, 1])
            elif not any(review.rating == 5 for review in result):
                result += self.get_mood_range(mood_lst=[4])
            elif not any(review.rating == 2 for review in result):
                result += self.get_mood_range(mood_lst=(1,))
            result.sort(reverse=True)
        return result

