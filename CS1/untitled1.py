# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:56:03 2024

@author: emyers26
"""
def main():
    def singsong():
        print("Hey")
        print("hi")
        
    singsong()
    singsong()
    singsong()
    singsong()
    
    secondlist = ["pizza", "corn", "meat",[4,3,5]]
    
    for i in range(len(secondlist)):
        for x in secondlist:
            print(x)
        print()
        
    thirdlist = ["six", "one", "three"] 
    for i in thirdlist:
        if(i=="six"):
            print(True)
           
        else:
            return False
 

main()