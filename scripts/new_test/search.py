import subprocess
import glob


def findApproxMatch(searchQuery):
    command = 'agrep'
    flags = '-i'
    searchQuery = searchQuery
    searchDir = "/home/yash/work/subtitle-data/"
    
    args = [command, flags,  searchQuery ] + glob.glob(searchDir+'*')
    output = subprocess.Popen( args, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
    print output


if __name__=='__main__':
    findApproxMatch('minimum safe distance')
