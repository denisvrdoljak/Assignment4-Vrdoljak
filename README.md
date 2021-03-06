# Assignment4-Vrdoljak
HW4
http://denisvrdoljak-w205-asn4.s3-us-west-1.amazonaws.com
Data Collection:
My data collection script generates all relevant combinations of hashtags (37 total) and days (30 total), then generates a url based search for each, for a total of 1,110 search queries. Then, it proceeds to simulate scrolling to the bottom of the page, using the Selenium library’s Firefox webdriver, 2,500 times per search. This gives a potential total of 2,775,000 pages of tweets. (Pages, as displayed in a browser, not API “pages.”)

Update: full dataset (well, only half the tags) has 507,030 tweets. WC2015-run1.csv is partial set, WC2015.csv is full set. Full set S3 address:
https://s3.amazonaws.com/denisvrdoljak-w205-asn2/HW4/WC2015.csv

The actual number was lower due to web-based rate limits and several hashtags having next to no tweets except on select days (non-English speaking, or at least tweeting, countries whereas this search was limited to only English language tweets.) The final number (still going, as I write this) should be around 400k.

Given a number of limitations, including needing my computer at times for ISVC, I wrote my script to stored completed hashtag/date combinations into a separate file (called done.txt), and check if completed on each pass. This allows me to stop (intentionally or otherwise) my process, and continue where I left off. Additionally, I make ample use of try/except methods to avoid corrupting any files with multiple potential ungraceful shutdowns.

To add another layer of resilience to the process, I prep the data to write to a file, and only briefly open, write, then immediately close the file to avoid a corrupted 400MB csv file. 

My process (and design choice) stores the tweet text, the url referenced, the date created (in YYYY-MM-DD format), and the hour of the day created. This lets me dump most of the irrelevant data that isn’t necessary for this analysis, such as location, user, retweets, etc.

Note: for some of the analysis below, I’m using a subset of tweets (about 60k) from the WWC, FIFA, and WorldCup hashtags to get started sooner.

Analysis

All my mappers break down what they are mapping into single item instances, which are then aggregated by the reducer. There is also code in there to extract the data from a local csv file, with a single function generating line-by-line data to simulate an EMR locally, returning one line for each relevant result, which my reducers reduce and aggregate, regardless of order returned.


Analysis 1:
On full set:
#aus		10107
#can		48923
#canwnt		13551
#chn		19484
#eng		48513
#fifa		75390
#fifawwc		81833
#football		11068
#fra		27119
#ger		47654
#jpn		12375
#ned		21985
#nzl		10832
#usa		127594
#uswnt		43215
#worldcup		43184
#wwc		29742
#wwc2015		45258
&		22463
-		40006

next would have been “2” with a count of 9219 (less than 10k)

Analysis 2:

The hourly breakdown of tweets for all 30 days, ordered, is in TweetsPerHour.txt, with a short sample here:
2015-07-04@1100hours		95
2015-07-04@1200hours		123
2015-07-04@1300hours		191
2015-07-04@1400hours		192
2015-07-04@1500hours		572
2015-07-04@1600hours		131
2015-07-05@1500hours		258
2015-07-05@1600hours		2482


UPDATE:
sample from full set:
2015-06-13@1000hours		456
2015-06-13@1100hours		1444
2015-06-13@1200hours		1093
2015-06-13@1300hours		1033
2015-06-13@1400hours		3617
2015-06-13@1500hours		1925
2015-06-13@1600hours		1830
UPDATE: full set in TweetsPerHour-FULLdataSET.txt



Analysis 3:

the top20 url’s (the ‘’ or blank being tweets with no url, followed by the next 20 highest counts) are, with frequency:
('', 61879)
('ift.tt/1bogwgx', 37)
('ift.tt/1hmxswm', 13)
('fifanews.ca', 11)
('nshnd.com/to.aspx?i=1264', 10)
('si.com/planet-futbol/', 9)
('nshnd.com/to.aspx?i=1263', 6)
('ift.tt/180r3yh', 6)
('nshnd.com/to.aspx?i=1261', 5)
('nshnd.com/to.aspx?i=1262', 5)
('youtu.be/dljet2ku33i', 4)
('nshnd.com/to.aspx?i=1255', 4)
('ift.tt/1gq30fw', 4)
('ift.tt/1bdxjtm', 4)
('twitter.com/ussoccer_wnt/s', 3)
('twitter.com/fifawwc/status', 3)
('cbsn.ws/1qtujnr', 3)
('bit.ly/1ioci8c', 3)
('goo.gl/gkqfks', 3)
('fifa.to/1iadffc', 3)
('theguardian.com/football/2015/', 3)



UPDATE: top 20 url’s (and counts) from full set (incl. no url/blanks):
('', 500141)
('fifanews.ca', 105)
('ift.tt/1bogwgx', 104)
('twitter.com/fifawwc/status', 47)
('tun.in/sfioz', 35)
('twitter.com/ussoccer_wnt/s', 35)
('passthelove.com', 23)
('goo.gl/kbqgkx', 22)
('streaming.radionomy.com/radiostaart', 20)
('mondelez.promo.eprize.com/passthelove15/', 18)
('nshnd.com/to.aspx?i=1264', 17)
('ift.tt/1hmxswm', 17)
('twitter.com/canadasocceren', 16)
('ift.tt/1bdxjtm', 15)
('goo.gl/1yfkub', 14)
('twitter.com/foxsoccer/stat', 14)
('si.com/planet-futbol/', 13)
('youtu.be/-uoo3lytrqu', 12)
('bit.ly/1t4ebpz', 11)
('twitter.com/bbcsport/statu', 11)
('fwd4.me/dwj', 10)

Analysis 4:

top 20 pairs (including with self):
words the with the occur 46608 times.
words #worldcup with #worldcup occur 36207 times.
words #wwc with #wwc occur 25029 times.
words to with to occur 19917 times.
words the with #worldcup occur 13658 times.
words #worldcup with the occur 13658 times.
words in with in occur 13512 times.
words the with #wwc occur 13092 times.
words #wwc with the occur 13092 times.
words the with to occur 10790 times.
words to with the occur 10790 times.
words for with for occur 10506 times.
words on with on occur 9756 times.
words in with the occur 9390 times.
words the with in occur 9390 times.
words world with world occur 8901 times.
words of with of occur 8879 times.
words #worldcup with to occur 7878 times.
words to with #worldcup occur 7878 times.
words and with and occur 7796 times.

<Using smaller dataset> There are 5,121,289 pairs of words in the smaller data set, meaning there would be 50 million in the larger one.

Note, above, not filtering for stop words for simplicity, and it doesn’t specify to.

ANALYSIS 5 (optional):

PMI = log( wordpairs[x-with-y]*len(wordpairs)/wordpairs[x-with-x]/wordpairs[y-with-y])

output:
PMI of #WWC and #WorldCup = 0.69314718056

using “#WWC” and “

QUESTION 1
The average length (using my partial run, while still waiting on the full run) is 106 characters. The most common length (mode) is 97 characters.

Tweet Length Mode (mode,count):  (97, 2246)
Tweet Length Mean:  106

The Median is approximately 103, indicating a pretty normal distribution, with a slight skew/tail to the right. This means that my partial sample, follows the Central Limit Theorem, as it should with 60k sample points, and would also be representative of the population of the entire dataset.

UPDATE: full set:
Tweet Length Mode (mode,count):  (138, 12973)
Tweet Length Mean:  108

As expected, the mean is very close to the sample from the partial set, though the mode changed a bit.


Question 2:
Sample until full dataset available:

Top 5 tweet tags (after only WWC and WorldCup):
#WorldCup 	37310 times
#WWC 	26130 times
Hashtag-Searched 	1 times ###CSV title/top row
***** END Top 5 tweet tags *****

UPDATE: from full set:

Top 5 tweet tags:
#USA 	95028 times
#FIFA 	72655 times
#FIFAWWC 	43668 times
#WorldCup 	37310 times
#CAN 	36601 times
***** END Top 5 tweet tags *****

UPDATE: Full list available in TopTags.txt

Can’t especially explain why Canada, a country with an entire population less than a single US state (ie California), is second…but the data says it is!

Question 3:
USA and Japan occur in the same tweet 165 times.

Question 4:
USA and Champion occur in the same tweet 0 times. (Guess that means we didn’t win.)

