"""
Module tests work of classes Review and ReviewList.
"""


from unittest import TestCase, main
from review_classes import Review, ReviewList

class TestReviews(TestCase):
    """Test class."""
    def setUp(self) -> None:
        self.review = Review(('Andy', 5, 'This is the best book, that I have \
ever read in my entire life! The plot is amazing and illustrations \
are fantastic.'))
        self.review2 = Review(('Andy', 3, 'This is not the best book, that I have \
read in my life. The plot is okay and illustrations are good.'))
        self.review3 = Review(('Andy', 3, "This is not the best book, that I've \
read in my life. The plot is okay and illustrations are good."))
        self.review4 = Review(('Alex', 2, "2.5 The book is freaking bad and dull"))
        self.review5 = Review(('Xena', 4, "Дуже крута книга. Рекомендую"))
        self.review6 = Review(('V', 1, 'slkлаб джedai linьлдж'))
        self.review7 = Review(('Anna', 2, 'This is a bad book.'))
        self.review8 = Review(('Xena', 4, "A very cool book. Read it!"))

    def test_correct_review(self):
        self.assertEqual(self.review.rating, 5)
        self.assertFalse(self.review.rating == 3)
        self.assertEqual(self.review.author, 'Andy')
        self.assertEqual(self.review.length, 116)
        self.assertEqual(self.review.neutrality, 0.602)
    
    def test_reviews_compare(self):
        self.assertFalse(self.review < self.review2)  # reviews with different rating
        self.assertTrue(self.review2 < self.review)
        self.assertFalse(self.review2 < self.review3)  # reviews with similar rating

    def test_add_review_list(self):
        reviews = ReviewList()
        reviews.add_review(self.review4)
        self.assertEqual(len(reviews.reviews), 0)  # Language of (2) could not be detect
        reviews.add_review(self.review5)
        self.assertEqual(len(reviews.reviews), 0)  # Doesn't add reviews not written in English
        reviews.add_review(self.review6)
        self.assertEqual(len(reviews.reviews), 0)

        reviews.add_review(self.review)
        self.assertEqual(len(reviews.reviews), 1)

    def test_review_list_sorting1(self):
        reviews = ReviewList()
        reviews.add_review(self.review7)  # rating: 2
        reviews.add_review(self.review2)  # rating: 3
        reviews.add_review(self.review)   # rating: 5
        reviews.reliability_sort()
        self.assertEqual(len(reviews.reviews), 3)
        self.assertEqual(reviews.reviews[0].rating, 5)
        self.assertEqual(len(reviews.get_mood_range()), 3) # reviews with rat. 5, 3, 2

    def test_review_list_sorting2(self):
        reviews = ReviewList()
        reviews.add_review(self.review8)  # rating: 4
        reviews.add_review(self.review2)  # rating: 3
        reviews.add_review(self.review7)  # rating: 2
        reviews.reliability_sort()
        self.assertEqual(len(reviews.reviews), 3)
        self.assertEqual(reviews.reviews[0].rating, 4)
        self.assertEqual(len(reviews.get_mood_range()), 3) # reviews with rat. 4, 3, 2

    def tearDown(self) -> None:
        return super(TestReviews, self).tearDown()


if __name__ == '__main__':
    main()