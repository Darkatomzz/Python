from elevenlabstts import generate, play



def elevenlabs_speak(text:str):
    audioobj =  generate.generate(text = text,
                         voice ='Bella',

    )
    play(audioobj)


elevenlabs_speak('ok')