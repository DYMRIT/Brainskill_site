import requests
from .models import TeleSetting


def sendTelegram(tg_name, tg_title, tg_text):
    settings = TeleSetting.objects.get(pk=1)
    token = str(settings.token)
    chat_id = str(settings.chat_id)
    text = str(settings.text)

    a = text.find('{na')
    b = text.find('me}')
    c = text.find('{ti')
    d = text.find('le}')
    e = text.find('{te')
    f = text.find('xt}')

    text_slise = text[0:a] + tg_name + text[b+3:c] + tg_title + text[d+3:e] + tg_text

    api = 'https://api.telegram.org/bot'
    met = api + token + '/sendMessage'
    req = requests.post(met, data={
        'chat_id': chat_id,
        'text': text_slise,
    })