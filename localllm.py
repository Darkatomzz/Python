import requests
#host = 'localhost:5000' #device and port


def Values(message):
    _request = {
        'character': 'SexyB',#characters must exist in your project make sure you type it correctly
        'history':'history',
        'mode':'chat',
        'chat-instruct_command':'Right away master, I will do whatever pleases you!',
        'prompt': message,
        'max_new_tokens': 250,
        'do_sample': True,
        'temperature': 0.7,
        'top_p': 0.5,
        'typical_p': 1,
        'epsilon_cutoff': 0,  # In units of 1e-4
        'eta_cutoff': 0,  # In units of 1e-4
        'repetition_penalty': 1.2,
        'top_k': 40,
        'min_length': 100,#testing
        'no_repeat_ngram_size': 0,
        'num_beams': 1,
        'penalty_alpha': 0,
        'length_penalty': 1,
        'early_stopping': False,
        'seed': -1,
        'add_bos_token': True,
        'truncation_length': 2048,
        'ban_eos_token': False,
        'skip_special_tokens': True,
        'stopping_strings': []
}

    responsefromdev =  requests.post(url="http://127.0.0.1:5000/api/v1/generate" ,json= _request)
    return responsefromdev                                  




def getlocalllmresponse(prompt:str)->str:
    result =  Values(prompt)
    if result.status_code == 200:
        text = result.json()['results'][0]['text']
        print(f"AI: {text}")
        return text
    else:
        print("Make sure you have the web-ui started\nHere are some helpful tips if it is!\nMake sure the url is correct")





