import os
import torch


def silero_tts(_tts_text:str,_sample_rate:int,_speaker:str):

    device = torch.device('cpu') #or 'cpu' or 'cuda' left it as cpu for compatability in case you don't have a nvidia gpu
    torch.set_num_threads(4)
    local_file = 'model.pt'

    if not os.path.isfile(local_file):
        torch.hub.download_url_to_file('https://models.silero.ai/models/tts/en/v3_en.pt',
                                    local_file)  

    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    audio_paths = model.save_wav(text=_tts_text,
                                speaker=_speaker,
                                sample_rate=_sample_rate)



    

    #example_text = text
    #sample_rate = sample_rate
    #speaker=speaker#'en_117'

    
  

  #silero_tts("Hello am just checking can you hear me",48000,'en_117')