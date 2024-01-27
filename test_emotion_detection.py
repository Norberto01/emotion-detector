import unittest
from EmotionDetection.emotion_detection import emotion_predictor

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        result = emotion_predictor("I am glad this happened")
        emotion = result['dominant_emotion']
        self.assertEqual(emotion, "joy")

        result = emotion_predictor("I am really mad about this")
        emotion = result['dominant_emotion']
        self.assertEqual(emotion, "anger")

        result = emotion_predictor("I feel disgusted just hearing about this")
        emotion = result['dominant_emotion']
        self.assertEqual(emotion, "disgust")

        result = emotion_predictor("I am so sad about this")
        emotion = result['dominant_emotion']
        self.assertEqual(emotion, "sadness")

        result = emotion_predictor("I am really afraid that this will happen")
        emotion = result['dominant_emotion']
        self.assertEqual(emotion, "fear")
    
unittest.main()