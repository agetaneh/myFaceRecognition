import os
import shutil
import random

source = '/home/pi/myFaceRecognition/images'
test = '/home/pi/myFaceRecognition/Data/Test'
train = '/home/pi/myFaceRecognition/Data/Train'
valid = '/home/pi/myFaceRecognition/Data/Validation'

#Get the dir that has all the images
files = os.listdir(source)

for eachFile in files:
    #Get all the images in the current directory
    img = os.listdir(source + '/' + eachFile)
    
    #Percent full numbers
    test_full = 0
    train_full = 0
    valid_full = 0

    #Random number from 0 to 10
    rand = 0

    #Number of images in directory
    num = len(img)

    #Number of files equivalent to the percent of total files
    p1 = num * .7
    p2 = num * .1
    p3 = num * .2

    
    for i in img:
        #Generate random num 0 - 10
        rand = random.randint(1, 100)
        
        #If the random was 7 or less(70%)
        if(rand <= 7):
            if(train_full < p1):
                shutil.copy(source + '/'+ eachFile + '/' + i, train + '/' + eachFile + '/' + i)
                train_full += 1
            elif(valid_full < p2):
                shutil.copy(source + '/' + eachFile + '/' + i, valid + '/' + eachFile + '/' + i)
                valid_full += 1
            else:
                shutil.copy(source + '/' + eachFile + '/' + i, test + '/' + eachFile + '/' + i)
                test_full += 1

        #This is the 20% range
        elif(rand > 7 and rand <= 9):
            if(valid_full < p2):
                shutil.copy(source + '/' + eachFile + '/' + i, valid + '/' + eachFile + '/' + i)
                valid_full += 1
            elif(train_full < p1):
                shutil.copy(source + '/'+ eachFile + '/' + i, train + '/' + eachFile + '/' + i)
                train_full += 1
            else:
                shutil.copy(source + '/' + eachFile + '/' + i, test + '/' + eachFile + '/' + i)
                test_full += 1

        #This is the 10% range
        else:
            if(test_full < p3):
                shutil.copy(source + '/' + eachFile + '/' + i, test + '/' + eachFile + '/' + i)
                test_full += 1
            elif(train_full < p1):
                shutil.copy(source + '/'+ eachFile + '/' + i, train + '/' + eachFile + '/' + i)
                train_full += 1
            else:
                shutil.copy(source + '/' + eachFile + '/' + i, valid + '/' + eachFile + '/' + i)
                valid_full += 1
