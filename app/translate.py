import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'MS_TRANS_KEY' not in app.config or \
            not app.config['MS_TRANS_KEY']:
                return _('Err: Translation service not configured')

    auth = {
            'Ocp-Apim-Subscription-Key': app.config['MS_TRANS_KEY'],
            'Ocp-Apim-Subscription-Region': 'westus',
    }
    r = requests.post(
            'https://api.cognitive.microsofttranslator.com'
            '/translate?api-version=3.0&from={}&to={}'.format(
                source_language, dest_language), headers=auth, json=[{'Text': text}])
    if r.status_code != 200:
        return _('Err: Translation service failed.')
    return r.json()[0]['translations'][0]['text']
