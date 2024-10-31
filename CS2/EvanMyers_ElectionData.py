#Evan Myers
#Description: A program that opens a file, removes useless words then writes the most important ones to an additional file.
#Bugs: There are reapeat words in the bad words list
#Features: None
#Sources: Python For Everybody
#Log 1.0 inital release

import string                     # gives acsess to the string functions
bw = ['them','these', 'than','by','from','or','out','every','were','more','then','ever','its','that','not','when','be','we','will','one','their','one','would','for','of','the','but', 'you', 'your', 'as','an','my','and','to','with','are','was','who','where','a','is','so','very','am','has','his','her','him','she','he','much','no','do','put','at','on','it','us','I','in','they','what','then','all','our','me','can','know','this','both','have','comes','come','may','whose','said','i']     # creates a list bw containing every bad word
fhand = open('trump_new.txt')    #opens the selected text file
counts = dict()             #assigns the variable counts to a dictonary
for line in fhand:
    # iterates through every word in the text and gets rid of all the words in the list and measures the freqency of each word
    line = line.rstrip()
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.lower()
    words= line.split()
    for word in words:
        # skips the word if it is inside the list and if it is not it gets tallied to its freqency
        if word in bw: 
            continue
        elif word not in counts:
            counts[word] = 1
        else:
            counts[word] +=1
file = open("election_stuff_trump.csv","w")            #opens new file            
for key,value in counts.items():
    # When the value of freqency is more than ten then it writes the word to the new file
    if value > 10:
        
        file.write(key + ","+ str(value)+"\n")


print(counts)  #print the word plus freqency to the csv file