from turtledemo.penrose import start

a = 6
a = a - 2
print(a*2)
a = a * 2
print(a+1)
a = a // 3
print(a)
print((3+10**2/2) or 70.0)
import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome("2704702208931031198668911301398022074072"))
print(palindrome("0974101607733149676776769413377061014790"))
print(palindrome("7798338247658278460338648728567428338977"))
print(palindrome("4257304920394478392772938744930294037524"))
def count_pattern_occurrences(text):
    '''
    finds occurrences that start with b, have unlimited letters and end in Bob

    :param text: the input where we will search for such occurrences
    :return:the number of matched words
    '''

    count=0 #I add a variable to keep the track of the occurrences and set it to 0
    start=0 #this parameter will help us to break or continue the operation and also serves as a starting point for searching
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

    return count
text="bobbyBob bObbBob, snansfjasnbBob bBobbybob bobB,ob"

print(count_pattern_occurrences(text))


text="My name is Bob and I live in Bob's house bobbyBobobo"

print(count_pattern_occurrences(text))

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
