#! /usr/bin/env python3.5
import shutil, os, subprocess, sys

argv = sys.argv

TVSHOWDIR = '/disks/hdd2/TV Shows'
TVSHOWDIRESCAPE = '/disks/hdd2/TV\ Shows/'
DOWNLOADDIR = '/var/lib/transmission-daemon/downloads'

#os.chdir('/home/bryan/Documents/Python/scan-download')

# uses subprocess instead
# output = os.popen('mv test test2').read()

os.chdir(DOWNLOADDIR)
for fromfolder in os.listdir():

        # grab the title and separating the periods to spaces
        foundseasontext = 0
        showtitle = ""
        namearray = fromfolder.split('.')[:-1]

        # once we have those strings split into arrays, we now need to determine whether it's an episode and season
        for word in namearray:
                wordarray = list(word)	
                print(wordarray)
		
                # check if it's a season/episode word
                if wordarray[0] == 'S' and wordarray[1].isdigit() == True:
                        # PASS but might need to more checks as we do not check for eps now. might fail if a title starts with S followed by a numeric value
                        print("Found Season")
                        foundseasontext = 1 
	 
                if foundseasontext:
                        # lets store all the words we had
                        next
                else:
                        # construct the title
                        if showtitle: 
                                showtitle = showtitle + " " + word
                        else:
                                showtitle = word

        # we got the title time to use it to serach
        
        print(showtitle)


        if (1):	
            os.chdir(TVSHOWDIR)
            for tofolder in os.listdir():
                if showtitle in tofolder:
                    print("Success: Found in" + TVSHOWDIR + "/" + showtitle)

                    fromdir = DOWNLOADDIR + "/" + fromfolder;

                    # we need to escape the folder
                    showtitleescape = showtitle.replace(" ","\ ")
                    todir = TVSHOWDIRESCAPE + "/" + showtitleescape + "/" + fromfolder

                    # os.rename(DOWNLOADDIR + "/" + fromfolder, TVSHOWDIR + "/" + fromfolder)
                    print("Trying to move" + fromdir + " TO " + todir )
                    # shutil.copyfile(fromdir,todir)
                    print('cp ' + fromdir + ' ' + todir)
                    os.popen('cp ' + fromdir + ' ' + todir).read()
                
