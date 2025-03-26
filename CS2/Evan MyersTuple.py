#Evan Myers
#Description: A program that Reads and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary, ounts the distribution of the hour of the day for each of the messages,  convert all the input to lower case and only count the letters a-z.
#Bugs: none 
#Features: none
#Sources:  https://www.py4e.com/code3/count3.py
#Log 1.0 inital release

import string
user_pick = input("Which exersice would you like to choose?")
if user_pick == "1":
    # opens the file and  sets the dictonary to counts
    fhand = open('tupleTxt.ini')
    counts = dict()
    # parses the data from each person and their address
    for line in fhand:
        line = line.lower()
        words = line.split()
    #count the number of messages from each person 
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    # Sort the dictionary by value
    lst = list()
    for key, val in list(counts.items()):
        lst.append((val, key))

        lst.sort(reverse=True)
    #prints the person with the most commits
    for key, val in lst[:1]:
        print(key, val)

elif user_pick == "2":
    file_name = r"tupleTxt.ini"
    hour_counts = {}                                                                            # create an empty dictionary to store hour count

    with open(file_name) as f:
        for line in f:
            if line.startswith("From "):                                                        # only process lines that start with "From "
                words = line.split()                                                            # split the line into words
                if len(words) > 5:                                                              # ensure there is enough data to get time
                    time_str = words[5]                                                         # extract time
                    hour = time_str.split(":")[0]                                               # split time with colon to get the hour
                    if hour in hour_counts:                                                     # count occurences of each hour
                        hour_counts[hour] += 1
                    else:
                        hour_counts[hour] = 1

    if hour_counts:                                                                             # after processing, sort and print results
        for hour in sorted(hour_counts.keys()):
            print(hour, hour_counts[hour])
            
            
elif user_pick == "3":
    letter_count = {letter: 0 for letter in string.ascii_lowercase}                             # create a dictionary to store letter count
    file_name = r"tupleTxt.ini"

    with open(file_name, 'r') as f:                                                             # open and process each line of file
        for line in f:
            line = line.lower()
            for char in line:
                if char in string.ascii_lowercase:                                              # check if character is a letter
                    letter_count[char] += 1

    sorter_letters = sorted(letter_count.items(), key = lambda x: x[1], reverse = True)         # sort dictionary by frequency in descending order

    for letter, count in sorter_letters:
        if count > 0:
            print(f"{letter}: {count}")                                                         # print the letters and their frequencies
else:
    print("invalid response, try again")