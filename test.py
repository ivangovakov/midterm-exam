def count_pattern_occurrences(text):
    '''
    finds occurrences that start with b, have unlimited letters and end in Bob

    :param text: the input where we will search for such occurrences
    :return:the number of matched words
    '''

    count=0 #I add a variable to keep the track of the occurrences and set it to 0
    start=0 #this parametr will help us to break or continue the operation and also serves as a starting point for searching
    while True: #I created a while True loop so the code runs until it breaks
        start=text.find('b', start) #first I check whether there is a "b" or not
        if start == -1: #if no more "b"s are found we break out of the operation
            break
#now we check if it ends with "Bob"
        end=text.find("Bob", start + 1) #this looks for "Bob" after "b"

        if end != -1: #If "Bob" was found after "b"
            count += 1 #Count this (+1)
            start = end+3 #move past this match
        else:
            break #if no valid "Bob" found after "b", stop searching

    return count #return the amount of occurrences we got
#to get the result printed use print(count_pattern_occurrences(text)). In brackets instead of text put the text you want to check for such occurrences, for example:

text="My name is Bob and I live in Bob's house bobbyBobobo"

print(count_pattern_occurrences(text))

list1=[1, 2, 3]
my_string=["hello"]
list1[0]=99 #we can change elements of the list
#string1[0]="H" this will cause error
#lalala

import random

random_numbers = [] # this generates a list of random numbers
for i in range(10):
    random_numbers.append(random.randint(1, 100))

for i in range(len(random_numbers)):  # this iterates through the list using indexes
    if random_numbers[i] > 50:
        random_numbers[i] = random.randint(20, 30) #this replaces numbers greater than 50 with a random number between 20 and 30﻿
    else:
        random_numbers[i] = "XX" #this replaces numbers lower than or equal to 50 with "XX"

print(random_numbers)


def is_valid_url(url):
    """
    Checks if the given string is a valid URL

    :param url: The string to check
    :return: True if valid URL, False otherwise
    """

   #this checks if the URL starts with "http://" or "https://"
    if not (url.startswith("http://") or url.startswith("https://")):
        return False  # Invalid if it does not start correctly

    #this ensures there is at least one '.' (dot) after the protocol
    dot_position = url.find(".", 8)  #the searching begins after "http://" or "https://"
    if dot_position == -1:
        return False  #there is no dot so the url is not valid

    # this checks that the URL ends with a common domain extension
    if not (url.endswith(".com") or url.endswith(".org") or url.endswith(".net") or url.endswith(".edu")):
        return False  #if it does not end with a known domain return false

    return True  # if url passed all of the checks, it is valid


print(is_valid_url("http://google.com"))
print(is_valid_url("https://example.org"))
print(is_valid_url("ftp://myserver.net"))


def days_since_birthday(birthday):
    """
    this function calculates how many days have passed since the birthday,
    considering only full years (excluding the birth year and the current year).

    :param birthday: The birthday in "DD-MM-YYYY" format.
    :return: The total number of days.
    """

    #this extracts the birth year from the birthday string
    birth_year = int(birthday[-4:])  # last 4 characters in date is year

    #get the current year we assume it's 2025 for this example
    current_year = 2025
    #the total days counter
    total_days = 0

    #loop through all full years between birth year and current year
    for year in range(birth_year + 1, current_year):
        #this checks if the year is a leap year (366 days) or normal year (365 days)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            total_days += 366  #for leap year
        else:
            total_days += 365  #for normal year

    return total_days


# Example usage:
print(days_since_birthday("12-06-2005"))

