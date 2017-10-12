#! /usr/bin/env python2.7

import requests, sys, webbrowser, bs4, urllib2, re

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

if (len(sys.argv) < 2) :
	print 'Only accepts a argument eg. ./scandownload.py <blah>'
	sys.exit()

argv = sys.argv

#print argv[1]
#print argv[0]

# sys.exit() # need to use closing and opening brackets 

res = requests.get('https://eztv.unblocked.bid/search/' + argv[1])
# res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,'html.parser')


#if (len(sys.argv) < 3):
	# if argv[2] == 'debug':
	#	debug = 1

#if debug:
	# print(soup.prettify())
#	print soup.find_all('a')
#	sys.exit()


# lets try find all links
if 1: 
	for link in soup.find_all('a'):
		thisLink = "Found " + link.get('href')
		# print(thisLink)		

		# need to find this link whether it contains magnet and matches the right string from the latest episode
		if re.search('magnet',thisLink):
			print "Found magnet in \n <<<" + thisLink + ">>> \n .. Trying to match"
			searchArray = re.search('magnet',link.get('href'))
		        print(searchArray)
			
			open(thisLink)

			# lets exit on first one
			sys.exit()
			
		# confirm donwload after that 
		

sys.exit()

# do not use the code below

# Open a browser tab for each result.
#linkElems = soup.find_all("a",{"class":"magnet"})
#linkElemsText = linkElems.text


if 0:
	for x in range(len(linkElems)):
		print linkElems[x].text

		searchObj = re.search( r'big.bang', linkElems[x].text, re.M|re.I)
		#searchObj = re.match(argv[1],linkElems[x].text)

		# once found, try to find the magnet link instead
		if searchObj:
			print ('Found!' + linkElems[x].text)
