HEADERLINE = "tweet-text" + "," + "tweet-url" + "," + "Year-Month-Day" + "," + "Hour" + "," + "Hashtag-Searched"

from collections import Counter
FILE_PATH = "/Users/denisvrdoljak/Berkeley/W205/Asn4_Work/WC2015-run1.csv"

def inputdatastream(filepath):
    with open(filepath) as csvfile:
        for line in csvfile:
            yield line


def generatehashtags():
    hashtags_list = ["#WWC",
    '#WorldCup','#FIFA','#CANWNT','#GERWNT','#JPNWNT','#SUIWNT','#GER',
'#FRAWNT','#MEXWNT','#USWNT','#USA','#FIFAWWC','#WWC2015','#AUSWNT','#ENGWNT','#FRA',
'#ENG','#CAN','#CHN','#NZL','#NED','#USA','#CIV','#NOR','#THA','#JPN','#SUI','#CMR',
'#ECU','#SWE','#AUS','#NGA','#BRA','#KOR','#ESP','#CRC','#COL'
    ]

    for hashtag in hashtags_list:
        yield hashtag


def tagmapper(filepath):
    import re
    taglist = list()
    try:
        for line in inputdatastream(FILE_PATH):
            if HEADERLINE in line:
                pass
            tweettext,tweeturl,tweetdate,tweethour,tweettag = line.split(",")
            taglist.append(re.sub('[,\t\n ]+', '', tweettag))
        return taglist
    except:
        return False




def urlmapper(filepath):
    urllist = list()
    try:
        for line in inputdatastream(FILE_PATH):
            tweettext,tweeturl,tweetdate,tweethour,tweettag = line.split(",")
            urllist.append(tweeturl)
        return urllist
    except:
        return False



def tweetlengthmapper(filepath):
    lengthlist = list()
    try:
        for line in inputdatastream(FILE_PATH):
            tweettext,tweeturl,tweetdate,tweethour,tweettag = line.split(",")
            lengthlist.append(len(tweettext))
        return lengthlist
    except:
        return False

print "######## stats, staring up, etc. ########"

#for tag in generatehashtags():
#    print tag, "\t\t", Counter(tagmapper(FILE_PATH))[tag]
print "######## done staring up, and stuff ########\n\n"

tagcounts = Counter(tagmapper(FILE_PATH))
print "Top 5 tweet tags:"
for toptag in tagcounts.most_common(5):
    t,c = toptag
    print str(t), "\t", str(c) + " times"
print "***** END Top 5 tweet tags *****\n\n"


print "Word URL's:"
urlcounts = Counter(urlmapper(FILE_PATH))
for urlstat in urlcounts.most_common(21):
    print urlstat
    tweetlenlist = tweetlengthmapper(FILE_PATH)
tweetstats = Counter(tweetlenlist)

print "Tweet Length Mode (mode,count): ", tweetstats.most_common(1)[0]
print "Tweet Length Mean: ", sum(tweetlenlist)/len(tweetlenlist)



def hourmapper(filepath):
    import re
    hourlist = list()
    try:
        for line in inputdatastream(FILE_PATH):
            if HEADERLINE in line:
                continue
            tweettext,tweeturl,tweetdate,tweethour,tweettag = line.split(",")
            timestamp = str(tweetdate+"@"+tweethour+"00hours")
            hourlist.append(timestamp)
        return hourlist
    except:
        return False

def wordmapper(filepath):
    import re
    wordlist = list()
    try:
        for line in inputdatastream(FILE_PATH):
            if HEADERLINE in line:
                continue
            tweettext,tweeturl,tweetdate,tweethour,tweettag = line.split(",")
            for word in tweettext.split():
                wordlist.append(word)
        return wordlist
    except:
        return False








def listwordpairs(textline):
    pairlist = list()
    for word in textline.split():
        for word2 in textline.split():
            if len(word)<2 or len(word2)<2:
                continue
            pairlist.append(str(word + " with " + word2))
    return pairlist


def wordpairmapper(filepath):
    wordpairs = list()
    try:
        for line in inputdatastream(FILE_PATH):
            if HEADERLINE in line:
                continue
            tweettext,tweeturl,tweetdate,tweethour,tweettag = line.split(",")
            for pair in listwordpairs(tweettext):
                wordpairs.append(pair)
        return wordpairs
    except:
        return False



print "Tweets by Hour:"
print type(hourmapper(FILE_PATH))

hourcounts = Counter(hourmapper(FILE_PATH))
hours = list(set((hourcounts)))
hours.sort()
for hour in hours:
    #print hour + "\t\t" + str(hourcounts[hour])
    pass

print "Word Counts (incl hashtags):"
wordcounts = Counter(wordmapper(FILE_PATH))
words = list(set((wordcounts.most_common(100))))
words.sort()
for word,c in words:
    if c < 10000:
        break
    print word + "\t\t" + str(wordcounts[word])

from collections import OrderedDict
x = OrderedDict(hourcounts)
#for hour in x:
#    print hour
#    break

#wordpairmapper
#ANALYSIS 4, QUESTION3, QUESTION4
print "Word Pairs:"
wordpairs = Counter(wordpairmapper(FILE_PATH))
print "Counter done"
#pairs = list(set((wordpairs.most_common(len(wordpairs)))))
#pairs.sort()
for pair,c in wordpairs.most_common(20):
    print "words",pair,"occur",c,"times."

print"\nUSA occurs with Japan", wordpairs["USA with Japan".lower()],"times."
print"\nChampion occurs with USA", wordpairs["Champion occurs with USA".lower()],"times."

print"\nJapan occurs with USA", wordpairs["Japan with USA".lower()],"times."
print"\nUSA occurs with Champion", wordpairs["USA occurs with Champion".lower()],"times."

#OPTIONAL, ANALYSIS5
print "PMI of #WWC and #WorldCup =",PMI(wordpairs,x,y)
PMC = 
wordpairs["#WWC with #WorldBup".lower()]/wordpairs["#WWC with #WWC".lower()]/

def PMI(resultsset,x,y):
    import math
    top = resultsset[str(x+" with "+y).lower()]*len(resultsset)
    bottom = resultsset[str(x+" with "+x).lower()]*resultsset[str(y+" with "+y).lower()]
    return (math.log(top/bottom))
