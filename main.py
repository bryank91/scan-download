#! /usr/bin/env python3.5
import shutil, os, subprocess, sys
from check_ep import * 


series = ["modern-family","young-sheldon","big-bang-theory","fresh-off-the-boat","westworld","silicon-valley"]
# serieswithdot = ["modern.family","young.sheldon","the.big.bang.theory","fresh.off.the.boat","westworld","silicon.valley"]
serieswithdot = ["young.sheldon","modern.family"]

for title in serieswithdot:
	answer = ""
	print("Finding: " + title)
	answer = getLatestEpisode('output.csv', title)
	print("Title: " + title + " : " + str(answer))
 

