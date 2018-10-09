import requests

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
    result = 0
    for x in range(numberOfTries):
        result += requests.get(totUrl).elapsed.total_seconds()

    result = result / x
    print("The Average Time :" + str(result) + " for tag : " + tag)
    return result

delay = "100"
delayInt = 0.100
user = "joarkarl100"
url = "http://130.243.27.198/auth/" + delay + "/" + user + "/"
averageCheckNumber = 30

tags = ["00" for x in range(16)]

x = 0
while x < 16:
    found = 0
    for i in range(0,16):
        for j in range(0,16):
            if found == 0:
                partOfTag = (hex(i)[2] + hex(j)[2])
                tags[x] = partOfTag
                thisTime = testTag(buildTag(tags))

                if thisTime > (delayInt * (x + 1)):
                    #Calculate the time again to make sure it is right
                    thisTime = testTagTimes(buildTag(tags), averageCheckNumber)
                    if thisTime > (delayInt * (x + 1)):
                        print ("Found " + partOfTag + " as index " + str(x) + " of tag")
                        found = 1

                if (thisTime < (delayInt * (x))) & (x > 0):
                    x = x - 1
    x = x + 1

print("    ")        
print(buildTag(tags))
print("done 😀")