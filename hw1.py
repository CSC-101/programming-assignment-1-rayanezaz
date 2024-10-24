import data
import math
from data import Employee

# Part 1
""""
This function takes a string and then returns the number of vowels (both upper and lower case)
from that string
"""

def vowel_count(data: str):
    firstList = list(data)
    secondList = []
    for x in firstList:
        if x in "aeiouAEIOU":
            secondList.append(x)
    return len(secondList)

# Part 2
""""
This function gets a list and, if the length is 2, then it will append that to a new list.
So, the the goal of this function is to return a list made up of nested lists with the length of 2.
"""""
def short_lists(data: list[list[int]]):
    firstList = []
    for x in data:
        if len(x) == 2:
            firstList.append(x)
    return firstList

# Part 3
"""""
In this function, there is a list full of nested lists, and if a list within has a length of 2,
then it will switch/replace the indexes if the first index is greater than the second index.
However, if the second index is not equal to 2, then the list will stay the way that it originally was.
In the end, the new list with nested lists is now returned
"""""
def ascending_pairs(data: list[list[int]]):
    firstList = []
    for x in data:
        if len(x) == 2:
            if x[0] > x[1]:
                firstList.append([x[1], x[0]])
            else:
                firstList.append(x)
        else:
            firstList.append(x)
    return firstList

# Part 4
"""""
In this function, there are dollars and cents. Ultimately, the function adds up the dollars and cents. However,
if the cents is greater than 99, then it will subtract 100 from cents, and then add 1 to dollars. After, it will return
the sum (the variable in which the sum is being returned is called sumPrice).
"""""
def add_prices(firstPrice, secondPrice):
    sumDollars = firstPrice.dollars + secondPrice.dollars
    sumCents = firstPrice.cents + secondPrice.cents
    while sumCents > 99:
        sumCents -= 100
        sumDollars += 1
    sumPrice = sumDollars + sumCents / 100
    return sumPrice

# Part 5
"""""
In this function, the top x is being subtracted from the bottom x. Then, the top y is being subtracted from the bottom y.
Then, both of these differences are subtracted to find the area of the rectangle
"""""
def rectangle_area(rectangle):
    firstSide = abs(rectangle.top_left.x - rectangle.bottom_right.x)
    secondSide = abs(rectangle.top_left.y - rectangle.bottom_right.y)
    return firstSide * secondSide

# Part 6
"""""
In this function, it inputs an author name and then the list of all the books made. From here, a loop will go through
each index in the list full of book class objects. It will check if one of the author names matches an author, and if it
does, then it will append the title of the book to the new list and then return the list
"""""
def books_by_author(authorName: str, authorBooks: list[data.Book]):
    firstList = []
    for book in authorBooks:
        if authorName in book.authors:
            firstList.append(book.title)
    return firstList

# Part 7
"""""
In this function, it will input an object from the rectangle class and then uses it from the top left and bottom right
points to calculate the distances between the points divided by 2 as well as the center point. The distances between the
points divided by 2 is the radius. From here, it will return the center and the radius
"""""
def circle_bound(rectangle):
    horizontalDistance = rectangle.top_left.x - rectangle.bottom_right.x
    verticalDistance = rectangle.top_left.y - rectangle.bottom_right.y
    circleCenter = (rectangle.top_left.x - (horizontalDistance / 2), rectangle.top_left.y - (verticalDistance / 2))
    circleRadius = math.sqrt(horizontalDistance ** 2 + verticalDistance ** 2)
    return round(circleRadius / 2, 2), circleCenter

# Part 8
"""""
In this function, it will input a list of employees, which is an employee class object. Then the function calculates
the average pay and the people that have a wage under the average. Then, they are inputted into a new list and they are
returned as a list of names
"""""
def below_pay_average(employees: list[Employee]):
    average = 0
    low = []
    for x in employees:
        average = average + x.pay_rate
    average = average/len(employees)
    for y in employees:
        if y.pay_rate < average:
            low.append(y.name)
    return low