#Evan Myers
#Description: A program that reads a data file and segments their catagories in a readable manner
#Bugs: none
#Features: none
#Sources: none
#Log 1.0 inital release
fhand = open("student_data_cs2.txt", 'r')                 #opens the data file and reads it
output_data = open("write_Student_Data.csv", "w")         #creates a new data file where the catagories are wirtten to
#iterates through the file and seperates the data by each section and takes unnecsery spaces away
for line in fhand:
  
    
    id = (line[0:6]).strip()
    
    
    fname = (line[6:21]).strip()
    
    
    lname = (line[21:36]).strip()
    
    
    grade = (line[36:42]).strip()
    
    
    gpa = (line [42:48]).strip()
   
    
    birthDate = (line [46:60]).strip()
   
    
    gender = (line [60:67]).strip()
  
    
    classRank = (line [67:76]).strip()
  
    
    attendencePercentage = line[76:86].strip()
    
    
    hnrs = (line [86:93]).strip()
 
    
    sports = (line [93:102]).strip()
   
    
    clubCount = (line [102:111]).strip()
    

  
    #outputs the data to the new csv file with commas seperating each of the data points
    output_data.write(id + ", " + fname + ", " + lname + ", " + grade + ", " + gpa + ", " + birthDate + ", " + gender + ", " + classRank + ", " + attendencePercentage  + ", " + hnrs + ", " + sports + ", " + clubCount + "\n")