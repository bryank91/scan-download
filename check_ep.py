#! /usr/bin/env python3.5
import shutil, os, subprocess, sys

argv = sys.argv

# Already declared in another function. However might be stil useful to have it here
TVSHOWDIR = '/disks/hdd2/TV Shows'
# TVSHOWDIRESCAPE = '/disks/hdd2/TV\ Shows/'
# DOWNLOADDIR = '/var/lib/transmission-daemon/downloads

def CheckEpisodes(dir):
    print('Walking...')
    for subdir, dirs, files in os.walk(dir):
        print('Processing...')
        for file in files:
            print(os.path.join(subdir, file))

def list_files(dir):                                                                                                  
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r

CheckEpisodes(TVSHOWDIR)
list_files(TVSHOWDIR)

