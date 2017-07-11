#!/usr/bin/python

import urllib2
import sys
import re
import os


wp_sites = []
file = ""


def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


def scan(url):
	try:
		print "Scanning !!! : "+str(url)
		tester = urllib2.urlopen(str(url)+"/post-a-job/").read()
		if('<form action="/post-a-job/" method="post" id="submit-job-form" class="job-manager-form" enctype="multipart/form-data">' in tester):
			print "  Vuln => : "+str(url)+"/post-a-job/"
			with open("Results.txt", "a") as f:
				f.write(url+"\n")
	except:
		pass

#Main
try:
	file = open(sys.argv[1]).readlines()
except :
	print "Usage : "+str(sys.argv[0])+" Exploit.py x.txt"
	sys.exit(1)
_=os.system("cls") , os.system('color c')
print '''

 __    __                                                      
/ / /\ \ \_ __         ###########################                                        
\ \/  \/ / '_ \        # Developer : DeMoN       #                                
 \  /\  /| |_) |       # Site : Guardiran.org    #                                   
  \/  \/ | .__/        # Tel : DarkCod3r         #                             
         |_|           ###########################                                        
   __        _                                                 
   \ \  ___ | |__     /\/\   __ _ _ __   __ _  __ _  ___ _ __  
    \ \/ _ \| '_ \   /    \ / _` | '_ \ / _` |/ _` |/ _ \ '__| 
 /\_/ / (_) | |_) | / /\/\ \ (_| | | | | (_| | (_| |  __/ |    
 \___/ \___/|_.__/  \/    \/\__,_|_| |_|\__,_|\__, |\___|_|    
                                              |___/            
   __            _       _ _                                   
  /__\_  ___ __ | | ___ (_) |_ ___ _ __                        
 /_\ \ \/ / '_ \| |/ _ \| | __/ _ \ '__|                       
//__  >  <| |_) | | (_) | | ||  __/ |                          
\__/ /_/\_\ .__/|_|\___/|_|\__\___|_|                          
          |_|                                                                  
		
		'''
if(len(file) > 0):
	
	
	for s in file:
		s = s.rstrip()
		scan(s)
	
	
		
print "Scan Result On Results.txt !"
