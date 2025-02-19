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

