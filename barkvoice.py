import os
import subprocess
os.environ["SUNO_OFFLOAD_CPU"] = "False"  # This tells Bark to use GPU instead of CPU
os.environ["SUNO_USE_SMALL_MODELS"] = "False"  # This tells Bark to use the full model CHANGE TO true if you have less than 12gb vram
from bark import SAMPLE_RATE, generate_audio,preload_models #you need atleast 8gb of vram for smaller model or 12 or above for larger model
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

print("Please wait preloading bark model!\nThis might take a few minutes......")
preload_models()


bestvoices = {
    "bestchinesemale":"v2/zh_speaker_0",
    "bestfemaleamericanspeaker":"v2/en_speaker_9",
    "bestfemalegermanspeaker":"v2/de_speaker_8"

}




def convert_wav_to_mp3(wavpath:str,mp3path:str):
    command = ['ffmpeg','-y','-i', wavpath, mp3path]
    subprocess.run(command)
    

converttomp3 = True
pathwav = "aigeneration.wav"
newmp3path = "voicenote.mp3"


def barkmodelhere():
    while True:
        textprompt = input("Enter prompt: ")
        audioarr = generate_audio(textprompt, history_prompt= bestvoices["bestchinesemale"])
        write_wav(pathwav,SAMPLE_RATE,audioarr)
        Audio(audioarr,rate=SAMPLE_RATE)
        if converttomp3:
                convert_wav_to_mp3(pathwav,newmp3path)
                if os.path.isfile(pathwav):
                    os.remove(pathwav)
                else:
                     print("File was probably deleted by user!")
     


def barkmodel(text:str):
        textprompt = text
        audioarr = generate_audio(textprompt, history_prompt= bestvoices["bestfemalegermanspeaker"])
        write_wav(pathwav,SAMPLE_RATE,audioarr)
        Audio(audioarr,rate=SAMPLE_RATE)
        if converttomp3:
            convert_wav_to_mp3(pathwav,newmp3path)
            if os.is_file(pathwav):
                    os.remove(pathwav)
            else:
                  print("File was probably deleted by user!")
            

#ALSO BARK IS ACTULY A LOT BETTER THAN WHAT PEOPLE THINK YOU MAY NEED TO RE-GENERATE A FEW TIMES TO GET A BETTER
#RESULT JUST LIKE STABLE DIFFUSION ALSO WHILST I CAN'T TALK ABOUT THE SMALLER MODEL THE LARGER MODEL WHICH I HAVE USED A LOT
#IS REALLY CONVINCING WITH SOME OF THE SPEAKERS IF YOU RUN THE LARGER MODEL MAKE SURE YOU HAVE ATLEAST 12GB OF VRAM

if __name__ == "__main__":
     barkmodelhere()