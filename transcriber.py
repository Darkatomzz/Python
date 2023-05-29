import whisper
import os
import sounddevice as sd
import soundfile as sf

wsprobj = whisper.load_model("base")

def RecordVoice(duration_length = 9,file_name = "recordingoutput.wav",samplerate = 44100):
    print("Recording Voice...")
    recording = sd.rec(int(duration_length * samplerate),samplerate=samplerate,channels=2)
    sd.wait()
    print("Finished recording!")
    sf.write(file_name,recording,samplerate) 

def ConvertAudioToMp3():
    os.system("ffmpeg -y -i recordingoutput.wav recordingoutput.mp3") # converts it to mp3 wont ask me if it wants to overwrite :
    #IMPORTANT YOU NEED FFMPEG INSTALLED ON YOUR COMPUTER IF YOU WANT TO CONVERT FILES 

    
def TranscribeAudio()->dict:
    result = wsprobj.transcribe("recordingoutput.mp3")#transcribe our audio
    print(f"Your audio was transcribed:{result['text']}")
    return result




def transcribeyourvoice():
    RecordVoice()
    ConvertAudioToMp3()
    TranscribeAudio()




if __name__ == "__main__":
    transcribeyourvoice()

