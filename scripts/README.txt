
testing voice to text using google speech using python scripts
=====================================

1. install pyAudio (required for recording audio) 
2. install FLAC command line tools from here: (https://xiph.org/flac/download.html). This command line tool is attached with the python scripts. 

FLAC tool will encode the .WAV recorded sound file into .FLAC file (lossless encoding for sound files) 



How to run:
1. Run py script: recordSound_as_WAV_example.py
The script is hardcoded to record a sound file for 3 seconds in .WAV format with file name sndClip.wav

2. Now run the attached flac tool to encode sndClip.wav to sndClip.flac 
flac -o sndClip.flac sndClip.wav

3. Now run gspeechToText_example.py as:
python gspeechToText_example.py
This script will send sndClip.flac file to google and the appropriate text will be returned in the JSON string.

** TODO **

- Integrate the separate tools in single package/module (record as WAV, conversion to FLAC and other convenient APIs)
- error handling 
- Integrate with CMU Sphinx since this is using the unofficial API from google. So will only work as long as google supports this on the hard coded URL used within the script. 



