import urllib2

def speectToText(filename='SendClip.flac'):
    url = "https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=en-US"
    audio = open(filename,'rb').read()
    headers={'Content-Type': 'audio/x-flac; rate=44100', 'User-Agent':'Mozilla/5.0'}
    request = urllib2.Request(url, data=audio, headers=headers)
    response = urllib2.urlopen(request)
    return response.read()
