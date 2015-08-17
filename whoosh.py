import os
import whoosh
import codecs
from whoosh.fields import Schema
from whoosh.index import create_in
from mappers import inputdatastream
from whoosh.fields import ID, KEYWORD, TEXT

FILEPATH = "/Users/denisvrdoljak/Berkeley/W205/Asn4_Work/ WC2015-2testing.csv"


my_schema = Schema(id = ID(unique=True, stored=True), 
                    path = ID(stored=True), 
                    tagsearch = ID(stored=True),
                    tags = TEXT(stored=True), 
                    date = TEXT(stored=True),
                    hour = TEXT(stored=True),
                    tweet = TEXT(stored=True))

writer = index.writer()
os.mkdir("twitterwwc-index")
index = create_in("wwc-index1", my_schema)

for i,line in enumerate(inputdatastream(FILEPATH)):
    print ".",
    writer.add_document( path = FILEPATH.encode("utf-8"),
                    tagsearch = line.split(",")[4].encode("utf-8"),
                    tags = [word for word in line.split(",")[0] if '#' in word], 
                    date = line.split(",")[2].encode("utf-8"),
                    hour = line.split(",")[3].encode("utf-8"),
                    tweet = line.split(",")[0].encode("utf-8"))
