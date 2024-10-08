# -*- coding: utf-8 -*-
"""Language_Translation_Tool.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LuzkxvxbBkZbOooPHHarZKXJDJZhcBeu
"""

!pip install requests google-cloud-translate azure-cognitiveservices-speech
!pip install langdetect

from google.cloud import translate_v2 as translate

def translate_text(text, target_language):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

import requests, uuid, json

def translate_text(text, target_language):
    subscription_key = 'YOUR_SUBSCRIPTION_KEY'
    endpoint = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0"
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': 'YOUR_REGION',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body = [{
        'text': text
    }]
    params = "&to=" + target_language
    response = requests.post(endpoint + params, headers=headers, json=body)
    return response.json()[0]['translations'][0]['text']

from langdetect import detect

def detect_language(text):
    return detect(text)

# Example function to translate text (using Google Translate API or another service)
def translate_text(text, target_language):
    # Assuming you have set up the API call
    # Here is a placeholder translation response
    return f"Translated '{text}' to {target_language}: 'Hola Mundo'"  # Replace with actual API call

# Ask for user input
text_to_translate = input("Enter the text you want to translate: ")
target_language = input("Enter the target language (e.g., 'es' for Spanish): ")

# Call the translate function and display the output
translated_text = translate_text(text_to_translate, target_language)
print(f"Translated text: {translated_text}")