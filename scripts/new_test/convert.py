import subprocess


def convertWavToFlac(filename='SendClip.wav'):
    output = subprocess.Popen(["flac", "--keep-foreign-metadata", filename]).communicate()[0]
    return output
