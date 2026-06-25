# Import the requests library to handle HTTP requests
import requests
import json

def emotion_detector(text_to_analyze):
   url = (
       'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   )

   headers = {
       "grpc-metadata-mm-model-id":
           "emotion_aggregated-workflow_lang_en_stock"
   }

   myobj = {
       "raw_document": {
           "text": text_to_analyze
       }
   }

   response = requests.post(url, json=myobj, headers=headers)
   # Parsing the JSON response from the API 
   formatted_response = json.loads(response.text)

   # Extracting emotions label and score from the response 
   emotions = formatted_response['emotionPredictions'][0]['emotion']

   # Find the dominant emotion
   dominant_emotion = max(emotions, key=emotions.get)

   # Add it to the dictionary
   emotions["dominant_emotion"] = dominant_emotion

   # Returning a dictionary containing only emotions and dominant emotion
   return emotions
