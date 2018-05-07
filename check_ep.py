#! /usr/bin/env python3.5
import shutil, os, subprocess, sys, csv

# Already declared in another function. However might be stil useful to have it here
TVSHOWDIR = '/disks/hdd2/TV Shows'
# TVSHOWDIRESCAPE = '/disks/hdd2/TV\ Shows/'
# DOWNLOADDIR = '/var/lib/transmission-daemon/downloads

def CheckEpisodes(dir,location,filename):
    count = 0

    for subdir, dirs, files in os.walk(dir):
        for file in files:
            location.append(os.path.join(subdir, file))
            filename.append(file)

            count += 1

    return(location,filename)

def list_files(dir):                                                                                                  
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r

def printCSV(csvfile,filename,location):
    #Assuming res is a flat list
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')

        arraylen = len(filename)

        for val in range(0,arraylen):
            writer.writerow([filename[val],location[val],identifyEp(filename[val])])    

    #Assuming res is a list of lists (Might be updated to support this in the future
    if 0:
        with open(csvfile, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(res)

    return 0

def identifyEp(filename):
	filearray = filename.split(".")
	for i in filearray:
		print(i + " - " + i[:1] + " - " +  i[1:2])
		if i[:1] is "S" and i[1:2].isdigit() is True:
			print("Pass")
			return i
			
	return 0	

def getLatestEpisode(filename,findstring):
	
	episodedigitarray = []
	
	with open(filename, "r") as output:
		csv_file = csv.reader(output, delimiter=",")
	
		for row in csv_file:
			if row[0].startswith(findstring) == True:
				episode = row[2][4:6]
				season = row[2][1:3]
				episodedigit = str(season) + str(episode);
				episodedigitarray.append(int(episodedigit))

	return(max(episodedigitarray))	
				

def main():

    # init
    filename = [];
    location = [];

    # (location,filename) = CheckEpisodes(TVSHOWDIR,location,filename)
    
    # printCSV('output.csv',filename,location)
    answer = getLatestEpisode('output.csv','Young.Sheldon')
    print(answer)



main()
