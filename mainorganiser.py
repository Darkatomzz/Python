import chatgpt as cgpt
import azuretts as ac
import json
import transcriber
import localllm as llm
import silerotest as si
import sounddevice as sd
from scipy.io.wavfile import read
import elevenlabstts
import requests
import recorder
import threading


azuecloudttsapikey = None
elevenlabsttsapikey = None 
openaiapikey = None
languagemodel = None # local language model or chatgpt :future character ai 
elevenlabsttsservice = False
azuecloudttsservice = False
silerottsservice = False
runlocallanguagemodel = False
runchatgptmodel = False
userconfigdict = None
canrun = False



def setupvars():
    global openaiapikey,elevenlabsttsapikey,azuecloudttsapikey,languagemodel,userconfigdict
    userconfigdict = getconfigs()
    if canrun is True:
        openaiapikey = userconfigdict['api_stuff']['openai_apikey']
        elevenlabsttsapikey = userconfigdict['api_stuff']['azure_cloud_tts']
        azuecloudttsapikey = userconfigdict['api_stuff']['azure_cloud_subscription_id']



def getconfigs()->dict:
    global canrun
    try:
     with open("userconfig.json" ,'r') as f:
          canrun = True
          return json.load(f)
    except Exception as f: 
        print("\nERRPR: Could not find the file or the filename: userconfig.json\nmake sure it's in the same directory\n{f}" )
        canrun = False


def determainettsservice():
    global elevenlabsttsservice,azuecloudttsservice,silerottsservice
    if userconfigdict['simple_user_config']['tts_service_to_use'] == 'azure_cloud_tts':
        azuecloudttsservice = True
    elif userconfigdict['simple_user_config']['tts_service_to_use'] == 'elevenlabs_tts':
        elevenlabsttsservice = True
    elif userconfigdict['simple_user_config']['tts_service_to_use'] == 'silero_tts':
        silerottsservice = True
    elif userconfigdict['simple_user_config']['tts_service_to_use'] == 'bark_tts':
        pass
    

    
def gettextfromaudio(convertomp3:bool = True)->str:#need to fix this in where if convertomp3 set to false it looks for mp3 file not wav :)
    transcriber.RecordVoice()
    if convertomp3:
        transcriber.ConvertAudioToMp3()
    voicetranscriptiondict = transcriber.TranscribeAudio()
    return voicetranscriptiondict['text']


def ttsservice(text:str):
    if azuecloudttsservice == True:
        ac.azuespeech(text,'18.00%')
    elif elevenlabsttsservice == True:
        elevenlabstts.elevenlabs_speak(f'{text}')
        
    elif silerottsservice == True:
        si.silero_tts(f"{text}",48000,'en_117')
        fs,data = read('test.wav')
        sd.play(data,fs)
        sd.wait()




def loaduplocalllm():
     llmresponse = llm.getlocalllmresponse(gettextfromaudio())
     determainettsservice()
     ttsservice(llmresponse)#18.00%

def loadupchatgpt():
    determainettsservice()
    ttsservice(cgpt.chatgptresponse(gettextfromaudio()))




def determainewhatmodeluserwants():
    global userconfigdict
    global runlocallanguagemodel
    global runchatgptmodel
    if userconfigdict['simple_user_config']['run_local_llm'] == 'true': 
        runlocallanguagemodel = True #run local llm
        loaduplocalllm()
    elif userconfigdict['simple_user_config']['run_chat_gpt_3.5'] == 'true':
        runchatgptmodel = True
        loadupchatgpt()
    else:
        print("Make sure you either have chatgpt or your llm set to true in the userconfig.json file!")


       


        

    

def main():
    setupvars() #Sort out some of our global vars and get user config stuff
    if canrun:
        determainewhatmodeluserwants()
    


if __name__ == '__main__':
    main()
    

'''
    
    



'''