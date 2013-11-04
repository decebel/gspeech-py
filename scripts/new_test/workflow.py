from record import recordWav
from convert import convertWavToFlac
from translate import speectToText
from jsonreader import readJson
from search import findApproxMatch


def mainWorkflow():

    recordWav()
    convertWavToFlac('SendClip.wav')
    response = speectToText('SendClip.flac')
    print response
    text = readJson(response)
    result = findApproxMatch(text)
    output = result[0].split('\r\n')
    print '---------------------'
    print 'RESULTS'
    print '---------------------'
    
    for out in output:
        print out
    print '---------------------'
    return

if __name__=='__main__':
    mainWorkflow()
