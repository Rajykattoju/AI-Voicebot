from gtts import gTTS
import os
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
class TTs:
    """ This class provides the method to convert Text obtained to speech"""
    @staticmethod
    def savemp3():
        """ This method saves the voice output as an mp3 file"""
        if(os.path.exists('tex.txt')):
            f=open('tex.txt',encoding='utf-8')
            tts=gTTS(text=f.read(),lang='en',slow=False)
            f.close()
            if(os.path.exists('sample.mp3')):
                os.remove('sample.mp3')
            tts.save('sample.mp3')
            os.remove('tex.txt')
        else:
            tts=gTTS(text="sorry couldn't get any results for what you are looking for",lang='en',slow=False)
            if(os.path.exists('sample.mp3')):
                os.remove('sample.mp3')
            tts.save('sample.mp3')
    @staticmethod
    def openmp3():
        """This method opens the Mp3 file and outputs the voice"""
        os.popen('sample.mp3')

            
