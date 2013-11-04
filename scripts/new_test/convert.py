import subprocess
import os

def convertWavToFlac(filename='SendClip.wav'):
    # Delete if filename exists
    lastindex = filename.rfind('.')
    newname = filename[0 : lastindex] + '.flac'
    os.path.exists(newname) and os.remove(newname)

    output = subprocess.Popen(["flac", "--keep-foreign-metadata", filename]).communicate()[0]
    return output
