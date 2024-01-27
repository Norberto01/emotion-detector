from flask import Flask

from EmotionDetection.emotion_detection import emotion_predictor

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def render_emotion():
    """
    Fetch emotion from api

    Returns:
        dictionary: message
    """    
    
    rv = emotion_predictor("I love my life")
    dominant_emotion = rv['dominant_emotion']
    msg = 'Invalid text! Please try again!'
    if dominant_emotion:
        msg = f"""
            For the given statement, the system response is 'anger': {rv['anger']},
            'disgust': {rv['disgust']}, 'fear': {rv['fear']}, 'sadness': {rv['sadness']}.
            The dominant emotion is {rv['dominant_emotion']}.
        """
    return {"message": msg}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
