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
    print '---------------------'
    print result
    print '---------------------'
    return

if __name__=='__main__':
    mainWorkflow()
