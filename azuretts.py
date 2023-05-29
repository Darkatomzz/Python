
import azure.cognitiveservices.speech as speechsdk






def azuespeech(text:str,pitch:str):
    global ssml_string
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription='yoursub', region='region')
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name='en-GB-SoniaNeural'#you can change the speaker here
    ssml_string = f"""
    <speak version='1.0' xmlns='https://www.w3.org/2001/10/synthesis' xml:lang='en-GB'>
      <voice name='en-GB-SoniaNeural'>
        <prosody pitch='{pitch}'>
          {text}
        </prosody>
      </voice>
    </speak>
    """

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Get text from the console and synthesize to the default speaker.
    speech_synthesis_result = speech_synthesizer.speak_ssml_async(ssml_string).get()

