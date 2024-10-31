#Evan Myers
#Description: 
#Bugs: There are reapeat words in the bad words list
#Features: None
#Sources: Python For Everybody
#Log 1.0 inital release

import string 
bw = ['them','these', 'than','by','from','or','out','every','were','more','then','ever','its','that','not','when','be','we','will','one','their','one','would','for','of','the','but', 'you', 'your', 'as','an','my','and','to','with','are','was','who','where','a','is','so','very','am','has','his','her','him','she','he','much','no','do','put','at','on','it','us','I','in','they','what','then','all','our','me','can','know','this','both','have','comes','come','may','whose','said','i']
fhand = open('trump_new.txt')
counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.lower()
    words= line.split()
    for word in words:
        if word in bw: 
            continue
        elif word not in counts:
            counts[word] = 1
        else:
            counts[word] +=1
file = open("election_stuff_trump.csv","w")            
for key,value in counts.items():
    if value > 10:
        
        file.write(key + ","+ str(value)+"\n")


print(counts)