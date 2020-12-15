import snscrape.modules.twitter as sntwitter
import csv
import timeit

keyword = '코로나'
month = 3

start_time = timeit.default_timer()

#Open/create a file to append data to
csvFile = open( str(month) + '_' + keyword + '.csv', 'a', newline='', encoding='utf8')

#Use csv writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['id','date','tweet']) 

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + 'since:2020-' + str(month) +'-01 until:2020-' + str(month + 1) + '-01 -filter:links -filter:replies').get_items()) :
    csvWriter.writerow([tweet.id, tweet.date, tweet.content])
csvFile.close()

end_time = timeit.default_timer()

print("%f s!!" % (end_time - start_time))