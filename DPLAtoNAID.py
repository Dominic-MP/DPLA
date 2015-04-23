import requests, json, argparse, datetime, csv, time

logfile = 'NAIDtoDPLA.csv'

url = 'http://api.dp.la/items/?api_key=10b516949e8a7bdc64f25903ee1aefd3&provider.name=%22National%20Archives%20and%20Records%20Administration%22&page_size=500'

r = json.loads(requests.get(url).text)

count = ( int(r['count']) / 500 ) + 3

print str(count) + ' pages'

page = 1

with open(logfile, 'w') as log :
	writelog = csv.writer(log, delimiter= '\t', quoting=csv.QUOTE_ALL)
	writelog.writerow( ('NAID', 'DPLA') )
	log.close()

while count > page :

	try:
		r = json.loads(requests.get(url + '&page=' + str(page)).text)
	except requests.exceptions.ConnectionError :
		print requests.get(url).status_code
		print requests.get(url).headers
		time.sleep(60)
		
	number = 0
		
	while number < 500 :
	
		with open(logfile, 'a') as log :
			writelog = csv.writer(log, delimiter= '\t', quoting=csv.QUOTE_ALL)
			writelog.writerow( (r['docs'][number]['originalRecord']['arc-id-desc'], r['docs'][number]['id']) )

		number = number + 1
	print 'Page ' + str(page) + ' complete'
	page = page + 1

log.close()
