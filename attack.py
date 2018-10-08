import requests

def buildTag(tags):
    resultTag = ""
    for tag in tags:
        resultTag += tag
    return resultTag

def testTag(tag):
    totUrl = url + tag
    result = requests.get(totUrl).elapsed.total_seconds()
    print(result)
    return result


delay = "999"
user = "joarkarl100"
url = "http://130.243.27.198/auth/" + delay + "/" + user + "/"

startTag = "01000000000000000000000000000000"
firstTime = requests.get(url + "startTag").elapsed.total_seconds()
print(firstTime)

tags = ["00" for x in range(16)]
tempTags = ["00" for x in range(16)]

lastTime = testTag(buildTag(tempTags))
prevTag = "00"

for x in range(16):
    found = 0

    #lägg in här, test om det är 00

    for i in range(1,16):
        lastTime = testTag(buildTag(tags))
        for j in range(1,16):
            if found == 0:
                partOfTag = (hex(i)[2] + hex(j)[2])
                tempTags[x] = partOfTag
                thisTime = testTag(buildTag(tempTags))
                print(buildTag(tempTags))

                if thisTime > (lastTime + 0.5):
                    print (partOfTag)
                    found = 1
                    tags[x] = partOfTag
                else :
                    prevTag = partOfTag
                    lastTime = thisTime
                    


print("    ") 
print("    ")        
print(buildTag(tags))
print("done 😀")