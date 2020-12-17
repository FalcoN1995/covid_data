# -*- coding: utf-8 -*-

import snscrape.modules.twitter as sntwitter
import csv
import sys

fir_arg = sys.argv[1]
sec_arg = sys.argv[2]
sec_arg = int(sec_arg)

keyword = fir_arg
month = sec_arg

# Open/create a file to append data to
csvFile = open( str(month) + '_' + keyword + '.csv', 'a', newline='', encoding='utf8')

# Use csv writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['id','date','tweet']) 

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + 'since:2020-' + str(month) +'-01 until:2020-' + str(month + 1) + '-01 -filter:links -filter:replies').get_items()) :
    csvWriter.writerow([tweet.id, tweet.date, tweet.content])
csvFile.close()
