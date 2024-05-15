#readfile.csv
sno     name        des
1       ravi        dev
2       sai         tester

import os
with open('readfile.csv', 'r') as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)
       
#To get the full path of the current working directory
#it prints the file working directory
import pathlib
print(pathlib.Path("text.csv").parent.absolute())

print(pathlib.Path().absolute())


#printing Random number in a list
import random
print(random.randint(0,9))


#coverting kilometers to miles
kilometers = float(input("enter value in kilometers:")
conv_fac = 0.621371
miles = kilometers * conv_fuc
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers, miles)



#To find the square root
num = 8
num_sqrt = num ** 0.5
print("the square root of %0.3f is %0.3f is %0.3f" %(num, num_sqrt))

