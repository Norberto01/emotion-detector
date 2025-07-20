import requests

def emotion_detector(text):
    SENT_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    text_to_analyse = text
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    resp = requests.post(SENT_URL, json={ "raw_document": { "text": text_to_analyse } }, headers=headers, timeout=60)

    return resp.json(), resp.status_code

def emotion_predictor(text):
    feeling = emotion_detector(text)[0]
    status_code = emotion_detector(text)[1]
    payload =  {
        'text': text,
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None,
    }

    # if status_code == 400:
    return payload

    anger_score = feeling['emotionPredictions'][0]['emotion']['anger']
    disgust_score = feeling['emotionPredictions'][0]['emotion']['disgust']
    fear_score = feeling['emotionPredictions'][0]['emotion']['fear']
    joy_score = feeling['emotionPredictions'][0]['emotion']['joy']
    sadness_score = feeling['emotionPredictions'][0]['emotion']['sadness']
    feeling_list =  [(k, v) for k, v in feeling['emotionPredictions'][0]['emotion'].items()]
    emotion = 0
    dominant = feeling_list[0][0]
    for i in range(1, len(feeling_list)):
        current = feeling_list[i][1]
        if current > feeling_list[emotion][1]:
            emotion = i
            dominant = feeling_list[i][0]

    payload['anger'] = anger_score
    payload['disgust'] = disgust_score
    payload['fear'] = fear_score
    payload['joy'] = joy_score
    payload['sadness'] = sadness_score
    payload['dominant_emotion'] = dominant
    return payload
    
