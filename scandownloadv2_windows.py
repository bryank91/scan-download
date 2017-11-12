#!python3.6

import requests, sys, webbrowser, bs4, re, os
# from balloontip.py import WindowsBalloonTip

from win10toast import ToastNotifier

'''
toaster = ToastNotifier()
toaster.show_toast("Hello World!!!",
              "Python is 10 seconds awsm!",
              duration=1)
toaster.show_toast("Hello World!!!",
             "Python is awsm by default!")
'''


#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

if (len(sys.argv) < 2):
	print('Only accepts a argument eg. ./scandownload.py <blah>')
	sys.exit()

argv = sys.argv

# we need to remove the first instance of an array as the array currently is grabbing nothing for some reason
argv.pop(0)

# before proceeding with the meat of the code, we need to grab the file
logFile = open('downloaded.txt')
logFileText = logFile.read()


for torrentLink in argv:
    # we need to convert all arguments to use full stops instead to be used later
    torrentLinkStrip = torrentLink.replace('-','.')

    res = requests.get('https://eztv.unblocked.bid/search/' + torrentLink)
    # res.raise_for_status()

    # Retrieve top search result links.
    soup = bs4.BeautifulSoup(res.text,'html.parser')

    # lets try find all links
    for link in soup.find_all('a', {'class':'download_1'}):
        thisLink = link.get('href')

        # lets split the word. once we've done that, we get the first 6 characters only
        episodeText = thisLink.split(torrentLinkStrip)[1]
        print('This is episode:' + episodeText[1:7])
        episodeTextNumber = episodeText[1:7]

        # combine both titles and episode to be used in the text file
        torrentCompare = torrentLinkStrip + '.' + episodeTextNumber

        # check if it exist in our download logger
        if torrentCompare in open('downloaded.txt').read():

            print('This torrent has been downloaded already:' + torrentCompare)
            continue # go to next link

        else:

            if thisLink:

                # we've found a link. time to download it by trying to open it
                # if re.search('magnet',thisLink):
                print("Found torrent link: \n" + thisLink + "\n")


                # once we downloaded those files, we would need to record what was downloaded onto a file


                '''
                if 0:
                    r = requests.get(thisLink)
                    with open("filename", "wb") as code:
                        code.write(r.content)
                    print("Download Complete!")
                '''

            # lets exit on first one only
            # sys.exit()
			
