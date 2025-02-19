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

