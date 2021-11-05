import requests
import json

#example output :
#{'url': 'https://pastebin.com/raw/pbs41biV', 'archived_snapshots': {'closest': {'status': '200', 'available': True, 'url': 'http://web.archive.org/web/20200606135541/https://pastebin.com/raw/pbs41biV', 'timestamp': '20200606135541'}}}
##

site = ''

def way(site) :

	#site = 'https://pastebin.com/raw/pbs41biV'

	url = 'http://archive.org/wayback/available?url='+site

	resp = requests.get(url)

	resp = resp.json()

	try :
		available = resp['archived_snapshots']['closest']['available']
	except :
		available = False

	if available == True :
		url = resp['archived_snapshots']['closest']['url']
		#print('Wayback Url Found : ' + url) 
		return '[+] Wayback Url Found : ' + url
	elif available == False :
		#print('No Dump On Way Back')
		return '[-] No Dump On Way Back'

#way(site)