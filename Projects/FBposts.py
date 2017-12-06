#https://nocodewebscraping.com/facebook-scraper/
#https://drive.google.com/file/d/0Bw1LIIbSl0xuRTNCZElUa3U1b1U/view

import urllib2
import json
import datetime
import csv
import time

#app_id = "1996698147270282"
#app_secret = "dda75b8506dbdc61c744d91394ec6841" # DO NOT SHARE WITH ANYONE!
page_id = raw_input("Please Paste Public Page Name:")

#access_token = app_id + "|" + app_secret

access_token = raw_input("Please Paste Your Access Token:")

def request_until_succeed(url):
    req = urllib2.Request(url)
    success = False
    while success is False:
        try: 
            response = urllib2.urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception, e:
            print e
            time.sleep(5)

            print "Error for URL %s: %s" % (url, datetime.datetime.now())
            print "Retrying."

    return response.read()

# Needed to write tricky unicode correctly to csv
def unicode_normalize(text):
    return text.translate({ 0x2018:0x27, 0x2019:0x27, 0x201C:0x22, 0x201D:0x22,
                            0xa0:0x20 }).encode('utf-8')

def getFacebookPageFeedData(page_id, access_token, num_statuses):
	
	# Construct the URL string; see http://stackoverflow.com/a/37239851 for 
	# Reactions parameters
	base = "https://graph.facebook.com/v2.6"
	mode = "/%s/posts" % page_id
	fields = "/?fields=message,link,permalink_url,created_time,type,name,id," + \
			"comments.limit(0).summary(true),shares,reactions" + \
			".limit(0).summary(true)"
	parameters = "&limit=%s&access_token-%s" % (num_statuses, access_token)
	url = base + node + fields + parameters
	
	#retrieve data
	data = json.loads(request_until_succeed(url))
	
	return data

def getReactionsForStatus(status_id, access_token):

	# See http://stackoverflow.com/a/37239851 for Reactions parameters
		# Reactions are only accessable at a single-post endpoint
	
	base = "https://graph.facebook.com/v2.6"
	node = "/%s" % status_id
	reactions = "/?fields=" \
			"reactions.type(LIKE).limit(0).summary(total_count).as(like)" \
			",reactions.type(LOVE).limit(0).summary(total_count).as(love)" \
			",reactions.type(WOW).limit(0).summary(total_count).as(wow)" \
			",reactions.type(HAHA).limit(0).summary(total_count).as(haha)" \
			",reactions.type(SAD).limit(0).summary(total_count).as(sad)" \
			",reactions.type(ANGRY).limit(0).summary(total_count).as(angry)"
	parameters = "&access_token=%s" % access_token
	url = base + node + reactions + parameters
	
	# retrieve data
	data = json.loads(request_until_succeed(url))