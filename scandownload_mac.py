#! /usr/bin/python

import requests, sys, webbrowser, bs4, urllib2, re

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

if (len(sys.argv) < 2) :
	print('Only accepts a argument eg. ./scandownload.py <blah> <episode> <filetype>')
	sys.exit()

argv = sys.argv
arglen = len(sys.argv) 

res = requests.get('https://eztv.unblocked.bid/search/' + argv[1])
# res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'html.parser')

if 1: 
	for link in soup.find_all('a', {'class':'download_1'}):
		thisLink = link.get('href')

		if 1:
			if arglen == 4: # only filetype is defined argv is defined
				if argv[2] in thisLink:
					if argv[3] in thisLink:
						print("Found torrent link: \n" + thisLink + "\n")
			elif arglen == 3:
				if argv[2] in thisLink:
					print("Found torrent link: \n" + thisLink + "\n")
					
			else:
				print("Found torrent link: \n" + thisLink + "\n")
		
			# once found, further refine by displaying size and season	
			
			if 0:	
				r = requests.get(thisLink)
				with open("/tmp/filename.torrent", "wb") as code:
				    code.write(r.content)
				print("Download Complete!");
	
# back tick these functions next time
# transmission-remote -n 'bryan:bryan' -a /var/lib/transmission-daemon/downloads/files.torrent	
