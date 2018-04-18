#! /usr/bin/python

# TODO : Add another argument to accept season and episode (eg. S0301)
# TODO : Only accept the lowest size file. SD probably
# TODO

# all the dependencies
import requests, sys, webbrowser, bs4, urllib2, re

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

if (len(sys.argv) < 2) :
	print('Only accepts a argument eg. ./scandownload.py <blah>')
	sys.exit()

argv = sys.argv

# grab url of the webpage
res = requests.get('https://eztv.unblocked.bid/search/' + argv[1])
# res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,'html.parser')


# lets try find all links
if 1: 
	for link in soup.find_all('a', {'class':'download_1'}):
		thisLink = link.get('href')
		# print(thisLink)		

		# need to find this link whether it contains magnet and matches the right string from the latest episode
		if 1:
		# if re.search('magnet',thisLink):
			print("Found torrent link: \n" + thisLink + "\n")
				
			# only if you checked magnets 
			#searchArray = re.search('magnet',link.get('href'))
		        #print(searchArray)
		
			r = requests.get(thisLink)
			with open("filename.torrent", "wb") as code:
			    code.write(r.content)
			print("Download Complete!");
	

			# lets exit on first one only
			sys.exit()
		


# back tick these functions next time
# transmission-remote -n 'transmission:transmission' -a /var/lib/transmission-daemon/downloads/files.torrent	
