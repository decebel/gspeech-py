import subprocess
import glob
from math import floor


def findApproxMatch(searchQuery, errorPercent=0.0):
    err = int(floor(errorPercent * len(searchQuery)))
    grep = 'agrep'
    flags = '-i'+str(err)
    searchQuery = searchQuery
    searchDir = "/home/yash/work/subtitle-data/*"

    command = grep + " " + flags + " " + "'" + searchQuery + "'" + " " + searchDir
    print 'Executing command: ' +command
    
    output = subprocess.Popen( command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
    print output


if __name__=='__main__':
    findApproxMatch('distao', 0.3)
