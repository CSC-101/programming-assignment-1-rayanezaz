import data
import hw1
import unittest

# Write your test cases for each part below.
class TestCases(unittest.TestCase):

    # Part 1
    def test_vowel_count(self):
        input = "writing"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(result, expected)

    def test_vowel_count2(self):
        input = "sequoia"
        result = hw1.vowel_count(input)
        expected = 5
        self.assertEqual(result, expected)

    # Part 2
    def test_short_lists(self):
        input = [[5], [7, 3], [9, 2, 45], [3, 1]]
        result = hw1.short_lists(input)
        expected = [[7, 3], [3, 1]]
        self.assertEqual(result, expected)

    def test_short_lists2(self):
        input = [[5, 3], [2, 5], [9], [43, 2, 53], [5, 2]]
        result = hw1.short_lists(input)
        expected = [[5, 3], [2, 5], [5, 2]]
        self.assertEqual(result, expected)

    # Part 3
    def test_ascending_pairs(self):
        input = [[5, 2], [5, 3, 9]]
        result = hw1.ascending_pairs(input)
        expected = [[2, 5], [5, 3, 9]]
        self.assertEqual(result, expected)

    def test_ascending_pairs2(self):
        input = [[-1, -9], [9, 2, 5], [4, 9], [3, 5, 9]]
        result = hw1.ascending_pairs(input)
        expected = [[-9, -1], [9, 2, 5], [4, 9], [3, 5, 9]]
        self.assertEqual(result, expected)

    # Part 4
    def test_add_prices(self):
        input = data.Price(9, 102)
        inputTwo = data.Price(5, 9)
        result = hw1.add_prices(input, inputTwo)
        expected = 15.11
        self.assertEqual(result, expected)

    def test_add_prices2(self):
        input = data.Price(1, 9314)
        inputTwo = data.Price(23, 364)
        result = hw1.add_prices(input, inputTwo)
        expected = 120.78
        self.assertEqual(result, expected)

    # Part 5
    def test_rectangle_area(self):
        input = data.Rectangle(data.Point(-5, 8), data.Point(-2, 10))
        result = hw1.rectangle_area(input)
        expected = 6
        self.assertEqual(result, expected)

    def test_rectangle_area2(self):
        input = data.Rectangle(data.Point(2, -4), data.Point(-3, 5))
        result = hw1.rectangle_area(input)
        expected = 45
        self.assertEqual(result, expected)

    # Part 6
    def test_books_by_author(self):
        bookList = [
            data.Book(["teddy", "larry", "carter"], "math"),
            data.Book(["teddy", "carter"], "english"),
            data.Book(["larry"], "science"),
            data.Book(["teddy"], "history")
        ]
        input = "teddy"
        inputTwo = bookList
        result = hw1.books_by_author(input, inputTwo)
        expected = ['math', 'english', 'history']
        self.assertEqual(result, expected)

    def test_books_by_author2(self):
        bookList = [
            data.Book(["teddy", "larry", "carter"], "math"),
            data.Book(["teddy", "carter"], "english"),
            data.Book(["larry"], "science"),
            data.Book(["teddy"], "history")
        ]
        input = "larry"
        inputTwo = bookList
        result = hw1.books_by_author(input, inputTwo)
        expected = ['math', 'science']
        self.assertEqual(result, expected)

    # Part 7
    def test_circle_bound(self):
        input = data.Rectangle(data.Point(-3, 2), data.Point(4, -5))
        result = hw1.circle_bound(input)
        expected = ((4.95), (0.5, -1.5))
        self.assertEqual(result, expected)

    def test_circle_bound2(self):
        input = data.Rectangle(data.Point(4, 8), data.Point(-3, 9))
        result = hw1.circle_bound(input)
        expected = ((3.54), (0.5, 8.5))
        self.assertEqual(result, expected)

    # Part 8
    def test_below_pay_average(self):
        employeeList = [
            data.Employee("thomas", 5),
            data.Employee("benjamin", 6),
            data.Employee("carl", 17),
            data.Employee("nicholas", 10),
            data.Employee("george", 12),
            data.Employee("abraham", 9),
            data.Employee("franklin", 8)
        ]
        input = employeeList
        result = hw1.below_pay_average(input)
        expected = ['thomas', 'benjamin', 'abraham', 'franklin']
        self.assertEqual(result, expected)

    def test_below_pay_average2(self):
        employeeList = [
            data.Employee("thomas", 7),
            data.Employee("benjamin", 2),
            data.Employee("carl", 13),
            data.Employee("nicholas", 14),
            data.Employee("george", 4),
            data.Employee("abraham", 9)
        ]
        input = employeeList
        result = hw1.below_pay_average(input)
        expected = ['thomas', 'benjamin', 'george']
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
